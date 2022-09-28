import os

def save(name, value):
    f = open("memstick/memory/" + str(name) + ".txt", 'w')
    f.write(str(value))
    f.close

def read(name):
    f = open("memstick/memory/" + str(name) + ".txt", 'r')
    return f.read()

def trash(name):
    os.remove("memstick/memory" + str(name) + ".txt")

