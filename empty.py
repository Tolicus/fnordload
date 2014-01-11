import time
import max7301
import signal
import sys

iodevice = max7301.MAX7301()
iodevice.set_pin_as_output(4)
iodevice.set_pin_as_output(5)
iodevice.set_pin_as_output(6)
iodevice.set_pin(6, 1)

def signal_handler(signal, frame):
    iodevice.set_pin(4, 0)
    iodevice.set_pin(5, 1)
    time.sleep(0.5)
    iodevice.set_pin(4, 1)
    iodevice.set_pin(5, 0)
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

for i in range(0, 30):
    iodevice.set_pin(6, 0)
    time.sleep(0.1)
    iodevice.set_pin(6, 1)
    time.sleep(0.1)
