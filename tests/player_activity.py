#!/usr/bin/env python

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import keys
import steam_tools

if __name__ == "__main__":

    s = steam_tools.steam_discover()

    # sys.setdefaultencoding('utf-8')

    friends = []
    response = s.get_friend_list(apikey=keys.steamwebapi, steamid='76561197999943351')

    print(len(response["friendslist"]["friends"]))

    for x in response["friendslist"]["friends"]:
        # print(x['steamid'])
        friends.append(x['steamid'])

    response = s.get_player_summaries(apikey=keys.steamwebapi, steamids=friends)

    print('{:10} {:30} {:38}'.format('State','Player', 'Game'))

    for x in response["response"]["players"]:
        y = '{:10} {:30} {:38}'.format(s.persona_state(x['personastate']), x['personaname'].encode('utf-8'), x['gameextrainfo'] if 'gameextrainfo' in x else '')
        print(y)

    # print(json.dumps(response, indent=4, sort_keys=True))