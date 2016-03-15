#!/usr/bin/env python3

from bottle import route, run, get, static_file, view, template
# from tinydb import TinyDB, where, Query

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

# Dynamic Routes
@route('/')
@route('/index.html')
@view('landing')
def index():
    return {'players':players}

@route('/players')
@view('players')
def players():
	return {'players':players}

@route('/hello')
def hello():
	return "Hello World!"

@route('/friends')
def friends():
	return static_file('friends.html', root='./')

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

# players = [{'steamid':'13241234','personaname':'muffin','gameextrainfo':'','timestamp':''},
# 		{'steamid':'13242342','personaname':'cupcake','gameextrainfo':'','timestamp':''},
# 		{'steamid':'23452345','personaname':'winklepop','gameextrainfo':'','timestamp':''},
# 		{'steamid':'12345234','personaname':'zoopzoop','gameextrainfo':'','timestamp':''}]


# @route('/<envelope:re:[a-zA-Z0-9]{6}>')
# @view('envelope')
# def envelope(envelope):
#     e = envelope.upper()
#     return db.search(q.envelope == e)[0]
#     # return dict(name=envelope, address_line_1='Line 1', address_line_2='Line 2')

# db = TinyDB('invites.json')

# q = Query()

# db.purge()
# db.insert({'envelope':'Q05UB5', 'name':'Mr T Bloking'})

run(host='0.0.0.0', port=8080, debug=True, reloader=True)

