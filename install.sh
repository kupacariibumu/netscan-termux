#!/bin/bash

# Color
N="\033[0m"
R="\033[0;31m"
G="\033[0;32m"
Y="\033[0;33m"
B="\033[0;34m"
P="\033[0;35m"
C="\033[0;36m"
LR="\033[91m"
LG="\033[1;32m"
LB="\033[1;34m"
LY="\033[1;33m"
LC="\033[1;36m"
LP="\033[1;35m"
RB="\033[41;37m"
GB="\033[42;37m"
BB="\033[44;37m"
BD="\033[1m"

colortext() {
  COLOR=$1
  echo -e "\033[${COLOR}${@:2}\033[0m"
}

clear

echo -e "[${LB}*${N}] ${B}Installing Netscan Termux${N}"
sleep 3
git clone https://github.com/mrpontora/netscan-termux.git
cd ~/netscan-termux
chmod +x netscan
mv netscan /data/data/com.termux/files/usr/bin/netscan
echo -e ""
echo -e "[${LB}*${N}] ${B}Installing package requirements${N}"
sleep 3
pip3 install .
cd
sleep 3
echo -e ""
echo -e "[${LG}✓${N}] ${G}Netscan Termux installed successful${N}"
sleep 3
echo -e ""
rm -r ~/install.sh