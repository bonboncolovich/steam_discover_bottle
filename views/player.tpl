
      %# This code block computes the css from the input dict
      %if player['gameextrainfo']:
        %friendblockcss = 'in-game'
        %playeravatarcss = 'in-game'
      %elif player['personastate'] is 'Online':
        %friendblockcss = 'online'
        %playeravatarcss = 'online'
      %elif player['personastate'] is 'Away':
        %friendblockcss = 'online'
        %playeravatarcss = 'online'
      %else:
        %friendblockcss = 'offline'
        %playeravatarcss = 'offline'
      %end

    <div class="friendBlock persona {{friendblockcss}}" href="{{player['profileurl']}}">
      <a class="friendBlockLinkOverlay " href="{{player['profileurl']}}"></a>
      <div class="playerAvatar {{playeravatarcss}}">
        <img src="{{player['avatar']}}" srcset="{{player['avatar']}} 1x, {{player['avatarmedium']}} 2x">
      </div>
      <div class="friendSmallText">
        {{player['personaname']}}<br/>
        {{'In-Game' if player['gameextrainfo'] else player['personastate']}}<br/>
        {{player['gameextrainfo']}}
      </div>
    </div>