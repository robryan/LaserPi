#!/bin/bash

# Set up a newly imaged Raspberry Pi for @robryan/LaserPi ...
# author: @robryan

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
# sudo apt-get -y install python3-pip 
# sudo pip install adafruit-io
# sudo pip install weather-api 

echo -e "\n finished Pi setup, rebooting ...\n"

# restart to make sure it's all available
sudo reboot

# return control to remote user
exit 1