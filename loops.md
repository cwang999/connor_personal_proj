human_space_travel = ["In what year did Neil Armstrong land on the moon?", "Which President cancelled the Apollo program?", "Which President authorized the Apollo program?", "How many space shuttles were built?", "Which space shuttle exploded in 1986?", "What is the name of NASA's first manned spaceflight program?", "Who was the first American in space?", "Which German and former-Nazi rocket scientist led the Apollo program?"]
human_space_answers = ["1969", "Richard Nixon", "John F. Kennedy", "5", "Challenger", "Mercury", "Alan Shepard", "Wernher von Braun"]

import random
def trivia(category):
  score = 0
  for i in range(num):
      print(human_space_travel[i])
      answer = input("Type your answer: ")
      correct = human_space_answers[i]
      if answer == correct:
        print("Correct!")
        score += 1
      else:
        print("Incorrect, moving on")
        
num = int(input("Please select the number of questions\n"))
score = trivia(category)
