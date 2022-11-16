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

# download Python libs
sudo apt-get -y install python3-pip 
sudo apt-get -y install python3-numpy 
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
