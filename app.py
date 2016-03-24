#!/usr/bin/env python

from bottle import route, run, get, static_file, view, template
import keys
import steam_tools

# Static Routes
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@get('/<filename:re:.*\.html>')
def html(filename):
    return static_file(filename, root='static/html')

# Dynamic Routes
@route('/')
@route('/index.html')
@view('landing')
def index():
    friends = []
    response = s.get_friend_list(apikey=keys.steamwebapi, steamid='76561197999943351')

    for x in response["friendslist"]["friends"]:
        friends.append(x['steamid'])
    
    players = s.get_player_summaries(apikey=keys.steamwebapi, steamids=friends)["response"]["players"]

    print(len(players))

    # Sanitize data, add human readable personastates
    for player in players:
        player['personastate'] = s.persona_state(player['personastate'])
        if 'gameextrainfo' not in player:
            player['gameextrainfo'] = ''
  
    # Sort players, move into steam_tools
    sorted_players = []
    for player in players:
        if player['gameextrainfo']:
            sorted_players.append(player)

    for player in players:
        if player['personastate'] is 'Online':
            if not player['gameextrainfo']:
                sorted_players.append(player)

    for player in players:
        if player['personastate'] is 'Away':
            if not player['gameextrainfo']:
                sorted_players.append(player)

    for player in players:
        if player['gameextrainfo']:
            continue
        if player['personastate'] is 'Online':
            continue
        if player['personastate'] is 'Away':
            continue
        sorted_players.append(player)

    players = sorted_players
    print(len(players))
    
    return {'players':players}

@route('/players')
@view('players')
def players():
    return {'players':players}

@route('/hello')
def hello():
    return "Hello World!"

rows = ['1','2','3','4','5']

players = [{
            "steamid": "76561197999943351",
            "communityvisibilitystate": 3,
            "profilestate": 1,
            "personaname": "bonbon",
            "lastlogoff": 1457338684,
            "profileurl": "http://steamcommunity.com/id/bonboncolovich/",
            "avatar": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/76/7683a0560246126a8d96224d3909a7268b41e8aa.jpg",
            "avatarmedium": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/76/7683a0560246126a8d96224d3909a7268b41e8aa_medium.jpg",
            "avatarfull": "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/76/7683a0560246126a8d96224d3909a7268b41e8aa_full.jpg",
            "personastate": 3,
            "realname": "Dan",
            "primaryclanid": "103582791430458876",
            "timecreated": 1216277750,
            "personastateflags": 0,
            "gameextrainfo": "Battle Islands"
            }]

if __name__ == "__main__":
    s = steam_tools.steam_discover()

    run(host='0.0.0.0', port=8080, debug=True, reloader=True)

