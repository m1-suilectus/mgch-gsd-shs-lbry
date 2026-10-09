from time import sleep

from magichome import MagicHomeApi

things = [
    MagicHomeApi("10.2.18.101", 1),
    MagicHomeApi("10.2.20.176", 1),
    MagicHomeApi("10.2.18.55", 1),
    MagicHomeApi("10.2.16.209", 1),
    MagicHomeApi("10.2.26.225", 1),
    MagicHomeApi("10.2.16.210", 1),
    MagicHomeApi("10.2.25.73", 1),
    MagicHomeApi("10.2.22.47", 1),
    MagicHomeApi("10.2.23.10", 1),
    MagicHomeApi("10.2.19.9", 1),
    MagicHomeApi("10.2.18.13", 1),
    MagicHomeApi("10.2.27.58", 1),
    MagicHomeApi("10.2.18.26", 1),
    MagicHomeApi("10.2.27.82", 1),
    MagicHomeApi("10.2.17.119", 1),
    MagicHomeApi("10.2.17.55", 1),
    MagicHomeApi("10.2.27.62", 1),
    MagicHomeApi("10.2.21.223", 1),
    MagicHomeApi("10.2.30.59", 1),
    MagicHomeApi("10.2.26.9", 1),
    MagicHomeApi("10.2.24.83", 1),
    MagicHomeApi("10.2.26.72", 1),
    MagicHomeApi("10.2.22.250", 1),
    MagicHomeApi("10.2.23.196", 1),
    MagicHomeApi("10.2.19.132", 1),
    MagicHomeApi("10.2.17.191", 1),
    MagicHomeApi("10.2.17.110", 1),
    MagicHomeApi("10.2.20.156", 1),
    MagicHomeApi("10.2.24.207", 1),
    MagicHomeApi("10.2.17.0", 1),
    MagicHomeApi("10.2.27.119", 1),
    MagicHomeApi("10.2.20.114", 1),
    MagicHomeApi("10.2.28.176", 1),
]

for Device in things:
    Device.turn_off()
