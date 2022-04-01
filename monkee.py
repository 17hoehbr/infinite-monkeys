import threading
import time
import random
import string
import names

solved = False

def typewriter(name):
    letters = []
    keystrokes = 0
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
        keystrokes = keystrokes + 1
    print("Monkey %s successfully composed Hamlet after %s attempts." % (name, attempts))
    solved = True

f = open('hamlet.txt', 'r')
hamlet = f.read()
hamlet = ''.join(ch for ch in hamlet if ch.isalnum())
hamlet = hamlet.lower()

monkeys = {}
while solved != True:
    for i in range(1):
        monkey = "monkey%d" % i
        monkeys[monkey] = threading.Thread(target=typewriter, args=(names.get_first_name(),))
    for i in monkeys:
        if not monkeys[i].is_alive():
            monkeys[i].start()