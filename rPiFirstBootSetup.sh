#!/bin/bash

# Set up a newly imaged Raspberry Pi for @robryan/LaserPi ...
# author: @robryan

# update device Unix libs
sudo apt-get update 
sudo apt-get -y upgrade 
sudo apt-get update 

# download Git
sudo apt-get -y install git 

# download LaserPi repo
git clone https://github.com/robryan/LaserPi.git 

# download Python libs
sudo apt-get -y install python-pip 
sudo pip install adafruit-io
sudo pip install weather-api 

# restart to make sure it's all available
sudo reboot