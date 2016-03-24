% rebase('base.tpl', title='landing')
<div class="profile_friends profile_manage_friends responsive_friendblocks">
  %print(len(players))
  %for player in players:
    %include('player.tpl', player = player)
  %end
</div>
