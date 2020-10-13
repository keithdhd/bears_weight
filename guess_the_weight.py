correct_weight = 50

guess = input("Guess the bear's weight: ")

if int(guess) == correct_weight:
  print("Well done! Correct")
elif int(guess) > 50:
  print("I'm lighter than that")
elif int(guess) < correct_weight and int(guess) > 40:
  print("I'm heavier than 40 but less than 51")
elif int(guess) < 40 and int(guess) > 30:
  print("Close! Try again")
else:
  print("I'm heavier than that")
