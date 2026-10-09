from time import sleep

from magichome import MagicHomeApi

DEVICES: dict = {
    1: MagicHomeApi("10.2.18.101", 1),
    2: MagicHomeApi("10.2.20.176", 1),
    3: MagicHomeApi("10.2.18.55", 1),
    4: MagicHomeApi("10.2.16.209", 1),
    5: MagicHomeApi("10.2.26.225", 1),
    6: MagicHomeApi("10.2.16.210", 1),
    7: MagicHomeApi("10.2.25.73", 1),
    8: MagicHomeApi("10.2.22.47", 1),
    9: MagicHomeApi("10.2.23.10", 1),
    10: MagicHomeApi("10.2.19.9", 1),
    11: MagicHomeApi("10.2.18.13", 1),
    12: MagicHomeApi("10.2.27.58", 1),
    13: MagicHomeApi("10.2.18.26", 1),
    14: MagicHomeApi("10.2.27.82", 1),
    15: MagicHomeApi("10.2.17.119", 1),
    16: MagicHomeApi("10.2.17.55", 1),
    17: MagicHomeApi("10.2.27.62", 1),
    18: MagicHomeApi("10.2.21.223", 1),
    19: MagicHomeApi("10.2.30.59", 1),
    20: MagicHomeApi("10.2.26.9", 1),
    21: MagicHomeApi("10.2.24.83", 1),
    22: MagicHomeApi("10.2.26.72", 1),
    23: MagicHomeApi("10.2.22.250", 1),
    24: MagicHomeApi("10.2.23.196", 1),
    25: MagicHomeApi("10.2.19.132", 1),
    26: MagicHomeApi("10.2.17.191", 1),
    27: MagicHomeApi("10.2.17.110", 1),
    28: MagicHomeApi("10.2.20.156", 1),
    29: MagicHomeApi("10.2.24.207", 1),
    30: MagicHomeApi("10.2.17.0", 1),
    31: MagicHomeApi("10.2.27.119", 1),
    32: MagicHomeApi("10.2.20.114", 1),
    33: MagicHomeApi("10.2.28.176", 1),
}

while True:
    NUM = int(input("Number: "))

    if DEVICES.get(NUM) is not None:
        DEVICE: MagicHomeApi = DEVICES.get(NUM)  # type: ignore
        try:
            DEVICE.turn_on()
            DEVICE.update_device(255, 0, 0, 0, 0)
            sleep(25)
        finally:
            DEVICE.turn_off()
