import random
class Die: 

 def __init__(self, eye):
  self.eye = eye
 
 def roll(self):
  self.eye = random.randint(1,6)
  
start_game = input ('Start die Game? Enter for start, q for quit')
if start_game != "q":
 Roll_dice = input ('Continue rolling? y or n') 
 d1 = Die(0)
 d2 = Die(0)
 
 while Roll_dice != "n":
  d1.roll()
  fv1 = d1.eye
  d2.roll()
  fv2 = d2.eye
  print(fv1)
  print(fv2)
  result = fv1+fv2
  print ("you roll: " + str(result))
  if result==7:
   print("************you win*************")
  else:
   print("----------------You lost------------")
  Roll_dice = input ('Continue rolling? y or n')  