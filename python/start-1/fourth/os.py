import os

if os.path.exists("famous_quotes.txt"):
    os.remove("famous_quotes.txt")
else:
    print("This file doesn't exist")
