# contains your implementation of algorithms
import random
from utility import *
import pathlib
import random
import string


# referred to as the brute force algorithm in week 2 slides
# idea here is to only limit solution space to words that match the feedback pattern of your most recent guess WHEN COMPARED WITH THE SOLUTION
def only_matched_patterns(current_guesses, guess_feedback, valid_solutions):
    remaining_solutions = []
    for word in valid_solutions:
        current_word_feedback = generate_feedback(current_guesses[-1], word)
        if current_word_feedback == guess_feedback[-1]:
            remaining_solutions.append(word)
    return random.choice(remaining_solutions)

###################################################################
def letter_frequency(current_guesses, guess_feedback, filtered_guesses):
  frequency1 = {}
  frequency2 = {}
  frequency3 = {}
  frequency4 = {}
  frequency5 = {}

  for word in filtered_guesses:
    if frequency1.get(word[0]) is None:
      frequency1[word[0]] = 1
    else:
      frequency1[word[0]] += 1

    if frequency2.get(word[1]) is None:
      frequency2[word[1]] = 1
    else:
      frequency2[word[1]] += 1

    if frequency3.get(word[2]) is None:
      frequency3[word[2]] = 1
    else:
      frequency3[word[2]] += 1

    if frequency4.get(word[3]) is None:
      frequency4[word[3]] = 1
    else:
      frequency4[word[3]] += 1

    if frequency5.get(word[4]) is None:
      frequency5[word[4]] = 1
    else:
      frequency5[word[4]] += 1

  current_solution = None
  current_score = 0
  potential_score = 0
  for word in filtered_guesses:
    word_letters = {}
    for i in word:
      if word_letters.get(i) is None:
        word_letters[i] = 1
      else:
        word_letters[i] += 1
    current_letter = None
    weighing = 1
    correct_weighing = 3
    misplaced_weighing = 1.3
    correct1 = set()
    correct2 = set()
    correct3 = set()
    correct4 = set()
    correct5 = set()
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][0] == "C":
        correct1.add(current_guesses[i][0])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][1] == "C":
        correct2.add(current_guesses[i][1])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][2] == "C":
        correct3.add(current_guesses[i][2])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][3] == "C":
        correct4.add(current_guesses[i][3])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][4] == "C":
        correct5.add(current_guesses[i][4])
    misplaced1 = set()
    misplaced2 = set()
    misplaced3 = set()
    misplaced4 = set()
    misplaced5 = set()
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][0] == "M" and current_guesses[i][0] not in correct1:
        misplaced1.add(current_guesses[i][0])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][1] == "M" and current_guesses[i][1] not in correct2:
        misplaced2.add(current_guesses[i][0])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][2] == "M" and current_guesses[i][2] not in correct3:
        misplaced3.add(current_guesses[i][0])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][3] == "M" and current_guesses[i][3] not in correct4:
        misplaced4.add(current_guesses[i][0])
    for i in reversed(range(len(current_guesses))):
      if guess_feedback[i][4] == "M" and current_guesses[i][4] not in correct5:
        misplaced5.add(current_guesses[i][0])
    total_misplaced = set().union(misplaced1).union(misplaced2).union(misplaced3).union(misplaced4).union(misplaced5)
    l1 = (frequency1[word[0]] / word_letters[word[0]] / len(filtered_guesses))
    if word[0] in correct1:
      l1 += weighing * correct_weighing
    elif word[0] in total_misplaced and word[0] not in misplaced1:
      l1 += weighing * misplaced_weighing
    l2 = (frequency2[word[1]] / word_letters[word[1]] / len(filtered_guesses))
    if word[1] in correct2:
      l2 += weighing * correct_weighing
    elif word[1] in total_misplaced and word[1] not in misplaced2:
      l2 += weighing * misplaced_weighing
    l3 = (frequency3[word[2]] / word_letters[word[2]] / len(filtered_guesses))
    if word[2] in correct3:
      l3 += weighing * correct_weighing
    elif word[2] in total_misplaced and word[2] not in misplaced3:
      l3 += weighing * misplaced_weighing
    l4 = (frequency4[word[3]] / word_letters[word[3]] / len(filtered_guesses))
    if word[3] in correct4:
      l4 += weighing * correct_weighing
    elif word[3] in total_misplaced and word[3] not in misplaced4:
      l4 += weighing * misplaced_weighing
    l5 = (frequency5[word[4]] / word_letters[word[4]] / len(filtered_guesses))
    if word[4] in correct5:
      l5 += weighing * correct_weighing
    elif word[4] in total_misplaced and word[4] not in misplaced5:
      l5 += weighing * misplaced_weighing
    potential_score = l1 + l2 + l3 + l4 + l5
    if potential_score == current_score:
      current_sum = 0
      potential_sum = 0
      potential_sum = frequency1[word[0]] + frequency2[word[1]] + frequency3[word[2]] + frequency4[word[3]] + frequency5[word[4]]
      current_sum = frequency1[current_solution[0]] + frequency2[current_solution[1]] + frequency3[current_solution[2]] + frequency4[current_solution[3]] + frequency5[current_solution[4]]
      if potential_sum >= current_sum:
        current_solution = word
      else:
        continue
    if potential_score > current_score:
      current_solution = word
      current_score = potential_score
  return current_solution