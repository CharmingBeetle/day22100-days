import random
print('THE ULTIMATE GUESS THE NUMBER GAME!')
print()
print('Try to guess the number between 0 and 1 million please. We will be keeping track of your guesses! You have 10 chances to guess!')

attempts = 1
true_number = random.randint(1, 1000000)
while attempts < 10:
  guess = int(input('What is your guess?:'))
  if guess < 0:
    print('Man, you are not even trying...Game over!')
    exit()
  if guess < true_number:
      print('Too low. Guess again!')
      attempts +=1
  elif guess > true_number:
      print('Too high. Try again')
      attempts += 1

  elif guess == true_number:
    print("Correct! You did an amazing job! You took", attempts, "attempts to answer.")
    break
else:
  print("What number is that?!")
print("You've made",attempts, "tries. Game over. The correct number was",true_number,".")
exit()



