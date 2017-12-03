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
from pprint import pprint
from datetime import datetime
import os
from vasiala_sender.utils import ensure_paths
from wxt5xx.comms import WXT5xx
from serial import Serial

from vasiala_sender.commandline import init


def run():
    from VaisalaSender_Serial import SerialConfig, ServicePort, Protocol, Address
    cache, archive = ensure_paths()

    device = WXT5xx(Serial(**SerialConfig), service_port=ServicePort, address=Address, protocol=Protocol)

    data = {
        "Time": datetime.utcnow().isoformat() + "Z",
        "Data": device.get_all_data()
    }

    device.reset_precipitation()
    device.close()

    cache_entry_path = os.path.join(cache, "%s.json" % data["Time"].replace(":", "_"))

    if not os.path.exists(cache_entry_path):
        with open(cache_entry_path, "w") as dout:
            json.dump(data, dout)


def main():
    init()
    run()

if __name__ == "__main__":
    main()
