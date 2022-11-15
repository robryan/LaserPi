#!/bin/bash

# Pull recent changes for @robryan/LaserPi

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

echo -e "pulling fresh LaserPi/master..."

# LaserPi repo should already exist, so just `git pull`
cd ./LaserPi/
# We don't care about local changes, just set Git config to fast-fwd to master, 
# because we've edited our changes on our nice Mac and pushed them up to GH
git config pull.ff only 
git fetch origin
git checkout master
git reset --hard origin/master
git pull 

echo -e "Pi now up to date with LaserPi/master ..."

echo -e "running servo test ..."

# servoTest.py has the code we just updated and want to run without opening a new SSH shell
python servoTest.py
