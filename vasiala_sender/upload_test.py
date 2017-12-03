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

import logging
from argparse import ArgumentParser
from datetime import datetime
from pprint import pprint

import os
import sensor_cloud
from sensor_cloud import UnivariateResult
from sensor_cloud.rest import ApiException
import sys

from vasiala_sender.commandline import init


def run():
    import VaisalaSender_SensorCloudConfig

    print sensor_cloud.configuration.password


    # sensor_cloud.configuration.username = 'nigel.bajema1@jcu.edu.au'
    # sensor_cloud.configuration.password = 'Krjyou8ag1Co5278Njw8'

    # sensor_cloud.configuration.username = 'nigel.bajema@gmail.com'
    # sensor_cloud.configuration.password = 'qwpo1209qwpo1209'


    api_instance = sensor_cloud.DefaultApi()
    streamid = 'jcu.test' # str |
    print datetime.now().isoformat()
    print datetime.utcnow().isoformat()+"Z"
    values = {"v": float('nan')}
    values2 = {"v": 28}
    results = [UnivariateResult(t=datetime.utcnow().isoformat()+"Z", v=values)]
    # results = [UnivariateResult(t="2015-11-12T00:00:00.000Z", v=values)]

    body = sensor_cloud.ObservationsPost(results=results) # ObservationsPost |

    # stream_body = sensor_cloud.StreamPost()
    FORMAT = '%(asctime)-15s %(levelname)-7s %(name)s %(filename)s:%(funcName)s:%(lineno)d - %(message)s'
    logging.basicConfig(format=FORMAT,level=logging.DEBUG)

    # hdlr = logging.StreamHandler(sys.stderr)
    # hdlr.setFormatter(logging.Formatter(FORMAT))
    # hdlr.setLevel(logging.NOTSET)
    # logging.root.addHandler(hdlr)

    pprint(body)
    if True:
        # try:
        # Upload observations for a stream
        api_response = api_instance.observations_post(streamid, body)
        # api_response = api_instance.locations_get(id="coen.vaisalia.1")
        # api_response = api_instance.streams_id_get("coen.vaisala.1.temperature", recursive=True)
        # api_instance.streams_id_put("jcu.test.2", )
        print type(api_response)
        print dir(api_response)
        print api_response.attribute_map
        pprint(api_response)
    # except ApiException as e:
    #     print("Exception when calling DefaultApi->observations_post: %s\n" % e)





if __name__ == "__main__":
    init()
    run()