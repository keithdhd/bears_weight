correct_weight = 50

guess = input("Guess the bear's weight: ")

if int(guess) == correct_weight:
  print("Well done! Correct")
elif int(guess) < correct_weight:
  print("I'm heavier than that")
else:
  print("I'm lighter than that")
