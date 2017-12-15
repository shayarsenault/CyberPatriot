#!/bin/bash
clear
echo GLHF
echo IF YOURE NOT IN ROOT EXIT AND sudo -s BEFORE STARTING
echo Enter password for root
read pass
echo installing expect if needed
sudo apt-get install Expect
clear
echo Done.
echo
echo
echo Enabling UFW
sudo ufw enable
# Uses expect to enter password
expect -c "
expect "password:"
send "$pass\r"
"
clear
echo Done
echo
echo
echo
echo Finding extensions
find /home -name "*.jpg" -delete
find /home -name "*.jpeg" -delete
find /home -name "*.mp3" -delete
find /home -name "*.mp4" -delete
find /home -name "*.ogg" -delete
#TODO Use sed to edit lightdm files


