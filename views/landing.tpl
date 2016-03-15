% rebase('base.tpl', title='landing')
<div>
  <h1>Steam Discover</h1>
  <tr>
    <th>Steam ID</th><th>Player Name</th><td>Current Game</th><th>Last Seen</th>
  </tr>
  </br>
  % for player in players:
  <tr>
  	<td>{{player['steamid']}}</td>
  	<td>{{player['personaname']}}</td>
  	<td>{{player['gameextrainfo']}}</td>
  	<td>{{player['timestamp']}}</td>
  </tr>
  </br>
  % end
</div>