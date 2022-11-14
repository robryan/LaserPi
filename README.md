# LaserPi

This project draws light art on glow-in-the-dark targets using a laser pointer and a Raspberry Pi. This repo is a fork of `tuckershannon/LaserPi`, and he deserves the props for the cool factor. 

## Requirements
To run this project, you'll need ... 
- a Raspberry Pi computer (I used a [RPi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/))
- Adafruit [pre-built servo gimbals](https://adafru.it/1967)


## Setup


1. **Image a fresh Raspberry Pi**. Use [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to set up a fresh SD card. Use the ⚙️ gear icon in the lower-right corner to add ... 
    - `hostname` of `raspberrypi.local`
    - ✅ enable `ssh` 
    - `username` / `password` to something non-default, [to avoid hackers](https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/)
    - ✅ `Configure wireless LAN` with valid WiFi creds

![handy imager options](./docs/rpi-imager-options.png)