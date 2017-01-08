__author__ = 'John'

import random

letters = 'abcdefghijklmnopqrstuvwxyz '
letter_len = len(letters)

# generates a random string of "string_length"
def generateRandomString(try_string, target_string, target_len):
    if len(try_string) == len(target_string):
        for i in range(target_len):
            if try_string[i] != target_string[i]:
                try_string[i] = letters[random.randrange(0, letter_len)]
    else:
        try_string = [letters[random.randrange(0, letter_len)] for i in range(target_len)]

    return try_string

def match_score(try_string, target_string):
    score = 0
    for i in range(len(try_string)):
        if try_string[i] == target_string[i]:
            score += 1
    return score

def monkey_type(target_string):
    best_score = 0
    best_string = ""
    targ_len = len(target_string)
    tries = 0

    while best_score < targ_len:
        for i in range(10):
            tries += 1
            best_string = generateRandomString(best_string, target_string, targ_len)
            score = match_score(best_string, target_string)
            if score > best_score:
                best_score = score
                print(''.join(best_string))
                if best_score == targ_len:
                    break

        print("Best Score So Far: " + str(best_score))
        print("Number of tries: " + str(tries))

monkey_type("to be or not to be that is the question weather it is nobler to suffer the slings and arrows")

