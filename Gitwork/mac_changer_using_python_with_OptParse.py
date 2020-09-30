import subprocess
import re
import optparse

def Arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i","--iface",dest="interface",help="interface whose mac is to be changed check interfaces by ifconfig command")
    parse.add_option("-m","--mac",dest="new_mac",help="new mac address")
    (options,arguments)  =  parse.parse_args()#this will return options(values) and arguments
    if not options.interface:
        parse.error("[+] write interface")
    elif not options.new_mac:
        parse.error("[+] write new mac address")
    else:
        return options
def change_mac(interface , new_mac):
    subprocess.call("ifconfig "+ interface + " down" ,shell = True)
    subprocess.call("ifconfig "+ interface +" hw ether "+new_mac ,shell = True)
    subprocess.call("ifconfig "+ interface+" up",shell = True)
    print("[+] mac changed: ......")
    ifconfig_results = subprocess.check_output("ifconfig "+interface ,shell = True)
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_results))
    return new_mac.group(0)   #return groups but we need first group only


def main():
        arguments = Arguments() #return arguments from Agruments() functions
        iface = arguments.interface
        new_mac_address = arguments.new_mac
        print("[+] changing to new mac.......")
        new_mac = change_mac(iface,new_mac_address)#new mac address return from change_mac() function
        print("[+] New mac address...   : "+new_mac)



main()