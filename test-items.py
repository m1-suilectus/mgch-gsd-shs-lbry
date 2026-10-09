from time import sleep

from magichome import MagicHomeApi

DEVICES: dict = {
    3: MagicHomeApi("10.2.18.55", 1),
    10: MagicHomeApi("10.2.19.9", 1),
    18: MagicHomeApi("10.2.21.223", 1),
    20: MagicHomeApi("10.2.26.9", 1),
}

while True:
    NUM = int(input("Number: "))

    if DEVICES.get(NUM) is not None:
        DEVICE: MagicHomeApi = DEVICES.get(NUM)  # type: ignore
        try:
            DEVICE.turn_on()
            DEVICE.update_device(255, 0, 0, 0, 0)
            sleep(10)
        finally:
            DEVICE.turn_off()
