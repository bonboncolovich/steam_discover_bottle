#!/usr/bin/env python

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from socket import *
from steam_tools import steam_discover

'''
Example of the target packet:

<start>
ff:ff:ff:ff:21:4c:5f:a0:	8  Packet fingerprint?
17:00:00:00:				4  Length of header 32bit int LE
08:f9:e6:b6:9c:ff:93:e9:	23 Header of message with type CMsgRemoteClientBroadcastHeader()
c4:5c:10:01:18:bb:cf:bc:
9f:8e:dc:a4:d3:b8:01:
40:00:00:00:				4  Length of body 32bit int LE
08:06:10:06:18:9c:d3:01:	64 Body of message with type CMsgRemoteClientBroadcastStatus()
22:04:54:49:4e:59:30:02:
38:10:40:01:4a:0b:09:b7:
6e:5d:02:01:00:10:01:10:
00:58:01:60:a0:ea:fa:b6:
05:68:00:70:00:7a:11:43:
38:2d:36:30:2d:30:30:2d:
31:45:2d:41:38:2d:34:45
<end>

Decoded header:
client_id: 6668041730191635321
msg_type: k_ERemoteClientBroadcastMsgStatus
instance_id: 13305483643707140027

Decoded body:
version: 6
min_version: 6
connect_port: 27036
hostname: "TINE"
enabled_services: 2
ostype: 16
is64bit: true
users {
  steamid: 76561197399943351
  auth_key_id: 0
}
euniverse: 1
timestamp: 1457435936
screen_locked: false
games_running: false
mac_addresses: "C8-60-00-1E-A8-4A"
'''

if __name__ == "__main__":

	s = steam_discover()

	soc=socket(AF_INET, SOCK_DGRAM)
	soc.bind(('',27036))

	while True:
		example_raw_packet = 'ff:ff:ff:ff:21:4c:5f:a0:17:00:00:00:08:f9:e6:b6:9c:ff:93:e9:c4:5c:10:01:18:bb:cf:bc:9f:8e:dc:a4:d3:b8:01:40:00:00:00:08:06:10:06:18:9c:d3:01:22:04:54:49:4e:59:30:02:38:10:40:01:4a:0b:09:b7:6e:5d:02:01:00:10:01:10:00:58:01:60:a0:ea:fa:b6:05:68:00:70:00:7a:11:43:38:2d:36:30:2d:30:30:2d:31:45:2d:41:38:2d:34:45'
		raw_packet = example_raw_packet.replace(':','')
		# raw_packet = soc.recv(1024)
	
		print(s.decode_packet(raw_packet))
		exit()


