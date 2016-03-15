<!-- % setdefault('player['gameextrainfo']', '') -->
<div class="friendBlock persona in-game" href="{{player['profileurl']}}" data-miniprofile="39039219">
  <a class="friendBlockLinkOverlay " href="{{player['profileurl']}}"></a>
  <div class="playerAvatar in-game">
    <img src="{{player['avatar']}}" srcset="{{player['avatar']}} 1x, {{player['avatarmedium']}} 2x">
  </div>
  <div class="friendSmallText linkFriend_in-game">
    {{player['personaname']}}<br />
    {{player['personastate']}}<br/>
    {{player['gameextrainfo']}}
  </div>
</div>