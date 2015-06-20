import random

from coerce import Coercion

class CoercionGame(object):
  def __init__(self, parent, chan):
    self.parent = parent
    self.chan = chan
    self.players = {}
    self.state = 'pregame'

  def tell_player(self, player, msg):
    self.parent.owner.send_privmsg(player, msg)

  def announce(self, msg):
    self.parent.owner.send_privmsg(self.chan, msg)

  def player_join(self, user):
    if user not in self.players:
      self.players[user] = CoercionPlayer(self, user)
      self.announce('{} has registered for the next game!')
    else:
      self.announce('{}: You are already registered.'.format(user))

  def player_quit(self, user):
    if user not in self.players:
      self.announce('{}: You are not registered!'.format(user))
    elif self.state == 'pregame':
      del self.players[user]
      self.announce('{} has been removed from the list of waiting players.')
    else: #if game is started
      #TODO: change the target of whoever is hunting this player
      pass

  def player_start(self, user):
    if self.state == 'pregame':
      if len(players) < Coercion.MIN_PLAYERS:
        self.announce('{}: We need at least {} players!'.format(user,
          Coercion.MIN_PLAYERS))
      else:
        self.announce('Starting a game with {} players!'.format(len(players)))
        self.assign_targets()
        self.assign_words()
        self.inform_players()
        self.state = 'running'
        self.announce('The game has now started!')
    else:
      self.announce('{}: The game is already in progress!'.format(user))

  def assign_targets(self):
    unused = set(self.players.keys())
    used = {}
    next = random.choice(unused)

    while unused:
      #prevents first player being assigned themselves
      target = random.choice(unused - {next})
      self.players[next].target = self.players[target]
      unused.remove(target)
      used.add(target)
      next = target

