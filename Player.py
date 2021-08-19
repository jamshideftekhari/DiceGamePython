import DieGame
class Player(object):
 def __init__(self, name):
     self.PlayerName = name
     self.Game = DieGame.DieGame()

 def PrintResult(self):
     self.Game.Play()
     self.Game.D1.roll()
     self.Game.D2.roll()
     self.Game.PrintResult()