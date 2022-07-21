import os 

# To get the full path to the directory a Python file is contained in, write this in that file:
dir_path = os.path.dirname(os.path.realpath(__file__))

# To get the current working directory use
cwd = os.getcwd()
print(cwd)