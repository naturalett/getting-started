default_greeting = "Hello World!"
filename = "../greeting.txt"


import sys

def askyesno(question):
    while True:
        answer = input(question + ' (y or n) ')
        if answer.upper() == "Y":
            return True
        if answer.upper() == "N":
            return False

def greet():
    with open(filename, 'r') as f:
        for line in f:
            print(line)



try:
    greet()
except OSError:
    print("Cannot read '%s'!" % filename, file=sys.stderr)
    if askyesno("Would you like to create a default greeting file?"):
        with open(filename, 'w') as f:
            print(default_greeting, file=f)
        greet()