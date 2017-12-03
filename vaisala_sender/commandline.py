import logging
from argparse import ArgumentParser

import os

import sys


def init():
    argParse = ArgumentParser(description="Serial Grabber will read the configured serial port and process the data received.")
    argParse.add_argument("--config-dir",metavar="<config_dir>", dest="config_dir", default="config", action="store", help="The location of the config directory, default: config")
    argParse.add_argument("-v", "--verbosity", default=0, action="count", help="increase output verbosity")
    args = argParse.parse_args()

    args.config_dir = os.path.abspath(args.config_dir)
    sys.path.append(args.config_dir)

    import VaisalaSender_SensorCloudConfig as SensorCloudConfig

    logging.TRACE = 5

    levels = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
        4: logging.TRACE,
        5: logging.NOTSET
    }
    if args.verbosity > 5:
        args.verbosity = 5
    logging.basicConfig(format=SensorCloudConfig.LOGGING_FORMAT,level=levels[args.verbosity])
    logging.addLevelName(logging.TRACE, "TRACE")