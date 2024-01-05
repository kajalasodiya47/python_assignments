# import random module
import random
f = open("test.txt","r")
# Return all lines in the file
lines = f.readlines()
# choose any random line
random_line = random.choice(lines)
print(random_line)
