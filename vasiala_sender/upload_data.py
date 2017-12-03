# Viasala Weather Station (WXT530) logger and uploader.
# Copyright (C) 2016  NigelB
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import json
import logging
import os
from pprint import pprint

import sensor_cloud
from datetime import datetime
from sensor_cloud import UnivariateResult

from vasiala_sender.constants import VaisalaConstants
from vasiala_sender.utils import ensure_paths
from vasiala_sender.commandline import init

logger = logging.getLogger("upload_data")

def post_observation(api_instance, id, value, sample_time):
    result= [UnivariateResult(t=sample_time, v=value)]
    body = sensor_cloud.ObservationsPost(results=result) # ObservationsPost |
    api_response = api_instance.observations_post(id, body)
    logger.log(logging.TRACE, "Result: %s"%api_response)

def post_wind(api_instance, config, entry, sample_time):
    try:
        wind_speed_average_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.WindSpeedAverage)
        wind_speed_min_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.WindSpeedMin)
        wind_speed_max_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.WindSpeedMax)

        wind_direction_average_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.WindDirectionAverage)
        wind_direction_min_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.WindDirectionMin)
        wind_direction_max_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.WindDirectionMax)

        speed_data = entry["Data"]["Speed"]

        direction_data = entry["Data"]["Direction"]


        if not speed_data["Average"][1] ==  "invalid":
            post_observation(api_instance, wind_speed_average_id, {"v":speed_data["Average"][0]}, sample_time)
        else:
            logger.warn("Speed Average Invalid!")

        if not speed_data["Limits"][0][1] ==  "invalid":
            post_observation(api_instance, wind_speed_min_id, {"v": speed_data["Limits"][0][0]}, sample_time)
        else:
            logger.warn("Speed Minimum Invalid!")

        if not speed_data["Limits"][1][1] ==  "invalid":
            post_observation(api_instance, wind_speed_max_id, {"v": speed_data["Limits"][1][0]}, sample_time)
        else:
            logger.warn("Speed Maximum Invalid!")



        if not direction_data["Average"][1] ==  "invalid":
            post_observation(api_instance, wind_direction_average_id, {"v":direction_data["Average"][0]}, sample_time)
        else:
            logger.warn("Direction Average Invalid!")

        if not direction_data["Limits"][0][1] ==  "invalid":
            post_observation(api_instance, wind_direction_min_id, {"v": direction_data["Limits"][0][0]}, sample_time)
        else:
            logger.warn("Direction Minimum Invalid!")

        if not direction_data["Limits"][1][1] ==  "invalid":
            post_observation(api_instance, wind_direction_max_id, {"v": direction_data["Limits"][1][0]}, sample_time)
        else:
            logger.warn("Direction Maximum Invalid!")

        return True

    except Exception as e:
        logger.exception("Failed to post data")

    return False


def post_ptu(api_instance, config, entry, sample_time):
    temp_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.Temperature)
    pressure_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.Pressure)
    humidity_id = "%s.%s"%(config.sensor_id_prefix, VaisalaConstants.Humidity)

    try:
        temp_value = {"v": float(entry["Data"]["Temperature"]["Ambient"][0])}
        temp_results= [UnivariateResult(t=sample_time, v=temp_value)]
        body = sensor_cloud.ObservationsPost(results=temp_results) # ObservationsPost |
        api_response = api_instance.observations_post(temp_id, body)
        logger.log(logging.TRACE, "Result: %s"%api_response)

        pressure_value = {"v": float(entry["Data"]["Pressure"][0])}
        pressure_results= [UnivariateResult(t=sample_time, v=pressure_value)]
        body = sensor_cloud.ObservationsPost(results=pressure_results) # ObservationsPost |
        api_response = api_instance.observations_post(pressure_id, body)
        logger.log(logging.TRACE, "Result: %s"%api_response)

        humidity_value = {"v": float(entry["Data"]["Humidity"][0])}
        humidity_results= [UnivariateResult(t=sample_time, v=humidity_value)]
        body = sensor_cloud.ObservationsPost(results=humidity_results) # ObservationsPost |
        api_response = api_instance.observations_post(humidity_id, body)
        print api_response
        logger.log(logging.TRACE, "Result: %s"%api_response)

        return True
    except Exception as e:
        logger.exception("Failed to post data")

    return False

def post_rain(api_instance, config, entry, sample_time):
    pass

def post_status(api_instance, config, entry, sample_time):
    pass

handlers = {
    "Wind": post_wind,
    "PTU": post_ptu,
    "Rain": post_rain,
    "Status": post_status
}

def run():
    from VaisalaSender_Serial import SerialConfig, ServicePort, Protocol, Address
    import VaisalaSender_SensorCloudConfig
    cache, archive = ensure_paths()

    api_instance = sensor_cloud.DefaultApi()

    cache_entries = os.listdir(cache)
    cache_entries.sort()
    for cache_entry_fn in cache_entries:
        with open(os.path.join(cache, cache_entry_fn), "r") as cach_entry_file:
            try:
                cach_entry  = json.load(cach_entry_file)
                for entry in cach_entry["Data"]:
                    logger.debug("Processing Entry: %s"%entry)
                    if entry["Type"] not in handlers:
                        logging.error("Handler not found for type: %s"%entry["Type"])
                    handlers[entry["Type"]](api_instance, VaisalaSender_SensorCloudConfig, entry, cach_entry["Time"])
            except Exception as e:
                logger.exception("Error handling: %s"%cache_entry_fn)

def main():
    init()
    run()

if __name__ == "__main__":
    main()