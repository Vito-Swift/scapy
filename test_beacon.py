from scapy.all import *

iface="edup-wlan0"
netSSID = 'fakeap' #Network name here

dot11 = Dot11(addr1='ff:ff:ff:ff:ff:ff',
        addr2='e8:4e:06:95:28:cd', addr3='e8:4e:06:95:28:cd')
beacon = Dot11Beacon(cap='ESS', timestamp=1)
essid = Dot11Elt(ID='SSID',info=netSSID, len=len(netSSID))

frame = RadioTap()/dot11/beacon/essid

frame.show()
print("\nHexDump of frame:")
hexdump(frame)

sendp(frame, iface=iface, inter=0.100, loop=1)
