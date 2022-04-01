import threading
import time
import random
import string
import names

def typewriter(name):
    letters = []
    attempts = 0
    while hamlet != letters:
        letter = random.choice(string.ascii_lowercase)
        if letter == hamlet[len(letters)]:
            letters.append(letter)
        else:
            letters.clear()
            attempts = attempts + 1
        if len(letters) >= 1:
            print("%s: %s\n" % (name, letters))
    solved = True
    print("Monkey %s successfully composed Hamlet after %s attempts." % (name, attempts))

f = open('hamlet.txt', 'r')
hamlet = f.read()
hamlet = ''.join(ch for ch in hamlet if ch.isalnum())
hamlet = hamlet.lower()
solved = False

monkeys = {}
while solved == False:
    for i in range(1):
        monkey = "monkey%d" % i
        monkeys[monkey] = threading.Thread(target=typewriter, args=(names.get_first_name(),))
        monkeys[monkey].start()