from random import randint
from time import sleep
from typing import List

from magichome import MagicHomeApi

DEVICES: List[MagicHomeApi] = [
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
    MagicHomeApi("127.0.0.1", 1),
]

Colors: List[tuple[int, int, int]] = []
for i in range(0, 25):
    x = i * 10 + 5
    Colors.append((x, x, x))

ColorsRGB: List[tuple[int, int, int]] = []
for i in range(0, 25):
    x = randint(0, 255)
    y = randint(0, 255)
    z = randint(0, 255)
    ColorsRGB.append((x, x, x))


def rotateForward():
    Colors.insert(0, Colors.pop())


def rotateForwardRGB():
    ColorsRGB.insert(0, Colors.pop())


Modes: dict = {1: "chase", 2: "pillars"}


for Device in DEVICES:
    Device.turn_on()
try:
    choice = str(input("Mode: "))
    while True:
        if choice == "1":
            while True:
                for Device in DEVICES:
                    Color = Colors[0]
                    Device.update_device(Color[0], Color[1], Color[2])
                    rotateForward()
                    sleep(0.025)
        elif choice == "2":
            i = 0
            for Device in DEVICES:
                Color = ColorsRGB[0]
                print(
                    f"Pillar {i + 1} has color: R = {Color[0]}, G = {Color[1]}, B = {Color[2]}"
                )
                i += 1
                Device.update_device(Color[0], Color[1], Color[2])
                rotateForwardRGB()

finally:
    for Device in DEVICES:
        Device.turn_off()
    exit(0)
