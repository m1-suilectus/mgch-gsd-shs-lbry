from typing import List

from magichome import MagicHomeApi

DEVICES: List[MagicHomeApi] = [
  MagicHomeApi("127.0.0.1", 5),
]

for Device in DEVICES:
  Device.turn_on() # turn on

  Device.update_device(5, 5, 5) # idk
