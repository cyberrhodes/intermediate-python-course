import random


def main():
  #roll = 5 
  dice_size = int(input('How many sides to the dice? ')) 
  dice_rolls = int(input('how many dice will be rolled? '))
  dice_sum = 0
  for i in range(0,dice_rolls):

    roll = random.randint(1,6)  
    dice_sum += roll 
    if roll == 1:
      print(f'roll: {roll} miss')
    elif roll == 6:
      print(f'roll {roll} hit')
    else: 
      print(f'else roll: {roll}') 
     
  print(f'The sum of your rolls: {dice_sum}')    

  print('"========================================"')





if __name__== "__main__":
  main()



