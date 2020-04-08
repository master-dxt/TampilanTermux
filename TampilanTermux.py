#!/bin/sh
#color

pkg update -y
pkg upgrade -y
pkg install cl -y
pkg install vim -y
pkg install ruby -y
gem install lolcat -y
pkg install cowsay -y
pkg install toilet -y
pkg install neofetch -y
pkg install nano -y
cd ../usr/etc

echo "masukan perintah........."
"nano bash.bashrc"
