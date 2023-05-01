import os
name='a'
file = open(name, "r")
details = [line.rstrip() for line in file.readlines()]
print(details)