import os

#Directories
data_logger_dir = None
if "APPDATA" in os.environ:
    data_logger_dir = os.path.join(os.environ["APPDATA"], "vdatalogger")
else:
    data_logger_dir = os.path.join(os.path.expanduser("~"), ".vdatalogger")

cache_dir = os.path.join(data_logger_dir, "cache")
archive_dir = os.path.join(data_logger_dir, "archive")