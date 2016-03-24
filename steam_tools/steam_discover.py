import requests
import json
import sys
import binascii
import struct

import steam_tools.steammessages_remoteclient_discovery_pb2


class steam_discover:

    def decode_packet(self, raw_packet):
        '''
        Decodes the protobuf broadcast message sent from steam clients to announce home streaming
        '''
        header = steammessages_remoteclient_discovery_pb2.CMsgRemoteClientBroadcastHeader()
        body = steammessages_remoteclient_discovery_pb2.CMsgRemoteClientBroadcastStatus()
        offset = 0

        packet = binascii.unhexlify(raw_packet)
        
        # print('Fingerprint: ' + binascii.hexlify(packet[0:8]))

        offset += 8
        length_header = struct.unpack_from('<i', packet, offset)[0]
        # print('Header length: ' + str(length_header))

        offset += 4
        # print(binascii.hexlify(packet[offset:offset + length_header]))
        header.ParseFromString(packet[offset:offset + length_header])
        # print('Header contents:\n' + str(header))

        offset += length_header
        length_body = struct.unpack_from('<i', packet, offset)[0]
        # print('Body length: ' +str(length_body))

        offset += 4
        # print(binascii.hexlify(packet[offset:offset + length_body]))
        body.ParseFromString(packet[offset:offset + length_body])
        # print('Body contents:\n' + str(body))

        return body

    def resolve_vanity_url(self):
        pass

    def get_friend_list(self, apikey='', steamid='76561197999943351', relationship='friend'):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Valve Steam Client;)'
        }

        url = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/'

        payload = {
                'key': apikey,
                'steamid': steamid,
                'relationship': relationship
        }

        page = requests.get(url, headers=headers, params=payload)

        return page.json()    

    def get_player_summaries(self, apikey='', steamids=[]):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Valve Steam Client;)'
        }

        url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'

        payload = {
                'key': apikey,
                'steamids': ','.join(map(str,steamids))
        }

        page = requests.get(url, headers=headers, params=payload)

        return page.json()

    def persona_state(self, personastate=0):

        state = ['Offline', 'Online', 'Busy', 'Away', 'Snooze', 'Looking to trade', 'Looking to play']

        return state[int(personastate)]

