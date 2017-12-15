#!/bin/bash
clear
echo GLHF
echo
echo
echo
echo
main(){
  echo Enter password for root
  read pass
  echo installing expect if needed
  sudo apt-get install Expect
  expect -c "
    expect "password:"
    send "$pass\r"
  "
  clear
  echo Done.
  echo
  echo
  echo Enabling UFW
  sudo ufw enable
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
  find / -name '.jpg'
}

main
