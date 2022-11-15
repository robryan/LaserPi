#!/bin/bash

# Set up a newly imaged Raspberry Pi for @robryan/LaserPi ...
# author: @robryan

echo "
   .~~.   .~~.
  '. \ ' ' / .'
   .~ .~~~..~.
  : .~.'~'.~. :
 ~ (   ) (   ) ~
( : '~'.~.'~' : )
 ~ .~ (   ) ~. ~
  (  : '~' :  ) Raspberry Pi
   '~ .~~~. ~'
       '~'"

echo -e "starting Raspberry Pi setup ..."

# update device Unix libs
sudo apt-get update 
sudo apt-get -y upgrade 
sudo apt-get update 

# download Git
sudo apt-get -y install git 

# download LaserPi repo
rm -rf ./LaserPi/
git clone https://github.com/robryan/LaserPi.git 

# set the rPI to use smoother "pigpio" servo lib bc "native" sucks
# https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-pin-factory
# [ -z "$GPIOZERO_PIN_FACTORY" ] && export GPIOZERO_PIN_FACTORY=pigpio

# download Python libs
sudo apt-get -y install python3-pip 
sudo pip install numpy
# sudo pip install adafruit-io
# sudo pip install weather-api 

# clean up extra Python libs
sudo apt autoremove

# download servo daemon library
sudo apt-get install pigpio python-pigpio python3-pigpio

echo -e "\n finished Pi setup, rebooting ...\n"

# restart to make sure it's all available
# return control to remote user
sudo reboot && exit 1
