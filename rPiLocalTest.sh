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

# re-download LaserPi repo
# yes ... it's inefficient but it also never has weird Git issues
rm -rf ./LaserPi/
git clone -q https://github.com/robryan/LaserPi.git

echo -e "Pi now up to date with LaserPi/master ..."

echo -e "running servo test ..."

# servoTest.py has the code we just updated and want to run without opening a new SSH shell
python LaserPi/servoTest.py

# return control 
exit 1