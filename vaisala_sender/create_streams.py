from argparse import Namespace
from pprint import pprint

import sensor_cloud

from vaisala_sender.commandline import init


def run():
    import VaisalaSender_SensorCloudConfig as SensorCloudConfig

    for stream in SensorCloudConfig.streams:
        stream_id = SensorCloudConfig.sensor_id_prefix+"."+stream
        # pprint(SensorCloudConfig.streams[stream])
        stream_data = Namespace(**SensorCloudConfig.streams[stream])
        print stream
        print stream_data.interpolationType
        body = sensor_cloud.StreamPost(stream_id,

                                       locationid=stream_data.location,
                                       organisationid=stream_data.organisation,
                                       sample_period=stream_data.samplePeriod,
                                       reporting_period=stream_data.reportingPeriod,
                                       stream_metadata=sensor_cloud.StreamMetadata(
                                           type=".ScalarStreamMetaData",

                                           observed_property=stream_data.observedProperty,
                                           unit_of_measure=stream_data.unitOfMeasure,
                                           interpolation_type=stream_data.interpolationType,
                                        ),
                                       resulttype="scalarvalue"
                                    )
        api_instance = sensor_cloud.DefaultApi()
        api_instance.streams_id_put(stream_id, body)

if __name__ == "__main__":
    init()
    run()