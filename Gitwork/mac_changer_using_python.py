

import subprocess
import re

def change_mac_address(interface,new_mac):
     print("[+] Changing to new mac.......")

     subprocess.call("ifconfig "+ interface + " down ",shell = True)
     subprocess.call("ifconfig "+ interface +" hw ether "+ new_mac,shell =True)
     subprocess.call("ifconfig "+ interface + " up",shell = True)
     print("[+] mac address changed to : "+new_mac)
     ifconfig_results = subprocess.check_output("ifconfig "+ interface , shell = True)
     new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_results))
     print(new_mac_address.group(0))

def main():
     subprocess.call("ifconfig ",shell = True)
     iface = str(input("enter interface: "))
     new_mac_address = str(input("enter new mac address: "))
     change_mac_address(iface , new_mac_address)

main()