import random


def main():
  dice_sum = 0   
  #roll = 5 
  dice_rolls = 2
  for i in range(0,dice_rolls):

    roll = random.randint(1,6)  
    dice_sum += roll 
    print(f'the number rolled: {roll}')
  print(f'The sum of your rolls: {dice_sum}')    

  #print('You rolled a die')
  print('"========================================"')
  print(dice_rolls)
  print(roll)

if __name__== "__main__":
  main()
