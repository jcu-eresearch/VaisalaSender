#!/usr/bin/env python
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

from setuptools import setup, find_packages

setup(name='ViasalaSender',
      version='0.0.1',
      description='Viasala Weather Station (WXT530) logger and uploader.',
      author='NigelB',
      author_email='nigel.blair@gmail.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=["pySensorCloud", "pyWXT5xx"],
      entry_points={
            "console_scripts": [
                  "vasiala_upload = vasiala_sender.upload_data:main",
                  "vasiala_create_sensor_streams = vasiala_sender.create_streams:main",
                  "log_data = vasiala_sender.log_data:main",
            ]
      }
)