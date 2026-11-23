import random


colours = ("red", "orange", "yellow", "green", "blue", "purple", "magenta", "brown", "black", "grey", "white")  
list = []
for i in range(0, 4):
  num = random.randint(0,10)
  colour = colours[num]
  list.append(colour)

  
for i in colours:
  print(i)


correct = 0
wrongplace = 0
totalguesses = 0
while correct != 4:
  guesses = []
  guess1 = input("\nA sequence including these colours has been generated.\nWhat do you think the first colour is?")
  guesses.append(guess1)
  guess2 = input("What do you think the second colour is?")
  guesses.append(guess2)
  guess3 = input("What do you think the third colour is?")
  guesses.append(guess3)
  guess4 = input("What do you think the fourth colour is?")
  guesses.append(guess4)
  totalguesses = totalguesses + 1
  
  correct = 0
  wrongplace = 0

  for i in guesses:
    position = guesses.index(i)
    if i == list[position]:
      correct = correct + 1
    elif i in list and i != list[position]:
      wrongplace = wrongplace + 1
  print("Fully correct:", correct)
  print("Wrong place:", wrongplace)
print("Well done, you have beaten the Mastermind! It took you", totalguesses, "guesses.")