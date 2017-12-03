import logging
import os


def ensure_paths():
    from VaisalaSender_Paths import cache_dir, archive_dir

    logger = logging.getLogger("Paths")

    logger.info("Cache Directory: %s"%cache_dir)
    logger.info("Archive Directory: %s"%archive_dir)

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    return cache_dir, archive_dir