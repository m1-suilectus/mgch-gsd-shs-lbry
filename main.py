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

def rotateForward():
  Colors.insert(0, Colors.pop())


for Device in DEVICES:
  Device.turn_on()
try:
  while True:
    for Device in DEVICES:

      Color = Colors[0]
      Device.update_device(Color[0], Color[1], Color[2])
      rotateForward()
    sleep(0.025)
finally:
  for Device in DEVICES:
    Device.turn_off()
