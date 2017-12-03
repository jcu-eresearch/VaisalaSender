from serial import EIGHTBITS, PARITY_NONE, STOPBITS_ONE

from wxt5xx.message import CommunicationProtocol


def config(**kwargs): return kwargs

SerialConfig = config(port="com3", baudrate=19200, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=1)

ServicePort = True

Protocol = CommunicationProtocol.ASCII_Polled_CRC

Address = None