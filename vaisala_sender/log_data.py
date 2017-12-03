import json
from pprint import pprint
from datetime import datetime
import os
from vaisala_sender.utils import ensure_paths
from wxt5xx.comms import WXT5xx
from serial import Serial

from vaisala_sender.commandline import init


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


if __name__ == "__main__":
    init()
    run()
