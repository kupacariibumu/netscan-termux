#!/usr/bin/env python
# -*- coding: utf-8 -*-

from source import request_api
import time
import os

red = ("\033[0;31m")
blue = ("\033[0;34m")
green = ("\033[0;32m")
yellow = ("\033[0;33m")
cyan = ("\033[0;36m")
magenta = ("\033[0;35m")
bold = ("\033[1;0m")
lightblue = ("\033[0;94m")

def main():
  menu()

def menu():
  try:
    print(bold + "============================================")
    print(lightblue + "▒█▄░▒█ ▒█▀▀▀ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▄░▒█")
    print(lightblue + "▒█▒█▒█ ▒█▀▀▀ ░▒█░░ ░▀▀▀▄▄ ▒█░░░ ▒█▄▄█ ▒█▒█▒█")
    print(lightblue + "▒█░░▀█ ▒█▄▄▄ ░▒█░░ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▒█░░▀█")
    print(bold + " 𝙷𝙰𝙲𝙺𝙴𝚁𝚃𝙰𝚁𝙶𝙴𝚃 𝚂𝙲𝚁𝙸𝙿𝚃 𝙼𝙾𝙳 𝙱𝚈 𝙼𝚁 𝙿𝙾𝙽𝚃𝙾𝚁𝙰 𝟸𝟶𝟸𝟸")
    print(bold + "============================================\n")
    print("[" + yellow + "01" + bold + "] Host To IP      [" + yellow + "06" + bold + "] Reverse IP Lookup")
    print("[" + yellow + "02" + bold + "] DNS Lookup      [" + yellow + "06" + bold + "] KP Location Lookup")
    print("[" + yellow + "03" + bold + "] Find DNS Host   [" + yellow + "08" + bold + "] Subnet Lookup")
    print("[" + yellow + "04" + bold + "] Find Shared DNS [" + yellow + "09" + bold + "] Extract Page Links")
    print("[" + yellow + "05" + bold + "] Reverse DNS     [" + yellow + "10" + bold + "] Exit Menu\n")
    
    choice = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Select Menu: " + bold)
    
    if choice == "01" or choice == "1":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "Host To IP Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      os.system("dig +short " + target)
      
    elif choice == "02" or choice == "2":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "DNS Lookup Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(2, target)
      print(txt)
      
    elif choice == "03" or choice == "3":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "Find DNS Host Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(3, target)
      print(txt)
      
    elif choice == "04" or choice == "4":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "Find Shared DNS Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(4, target)
      print(txt)
      
    elif choice == "05" or choice == "5":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "Reverse DNS Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(5, target)
      print(txt)
      
    elif choice == "06" or choice == "6":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "Reverse IP Lookup Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(6, target)
      print(txt)
      
    elif choice == "07" or choice == "7":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "IP Location Lookup Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(7, target)
      print(txt)
    
    elif choice == "08" or choice == "8":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "Subnet Lookup Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(8, target)
      print(txt)
      
    elif choice == "09" or choice == "9":
      print(bold + "\n[" + yellow + "+" + bold + "] " + blue + "Extract Page Links Option")
      target = input(bold + "[" + yellow + "+" + bold + "] " + blue + "Target: " + bold)
      print()
      txt = request_api.request_api(9, target)
      print(txt)
    
    elif choice == "10":
      exit()
    
    else:
      print(bold + "\n[" + red + "!" + bold + "] " + yellow + "Invalid Input")
      print(bold + "[" + red + "!" + bold + "] " + yellow + "Netscan Aborted")
      exit()
      
  except KeyboardInterrupt:
    print(bold + "\n[" + red + "!" + bold + "] " + yellow + "Netscan Aborted")
    exit()
  
main()