import random
d1 = 0
d2 = 0
res = 0
results = []

def rol_dice():
 global d1 
 d1 = random.randint(1,6)
 print ("dice 1:", d1)
 global d2 
 d2 = random.randint(1,6)
 print ("dice 2:", d2)

def print_result():
 global res 
 res = d1+d2
 print( "result: ", res)

def print_winner():
 global res
 if res == 7:
  print ("**** Hura *** you Win")
 else:
  print ("**** you loose ****")

def print_statistic():
 win = 0
 loose = 0
 for res in results:
  if res==7: win+=1
  else: loose+=1
  print (res) 
 print ("you won %d times" %win)
 print ("you loose %d times" %loose)


keyInput = input( "roll the dice? press enter to continue, q for quite " ) 
while keyInput != "q":
 rol_dice()
 print_result()
 print_winner()
 results.append(res)
 keyInput = input( "roll the dice? q for quite " ) 

print ("reslts:")
print_statistic() 
print ("*************game over*****************" )