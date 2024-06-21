import os
if os.path.isfile("config.txt"):
    l_file = open("config.txt", "r")
    __points = int(l_file.readlines()[0])*10


def points_up():
    global __points
    __points += 10


def points_down():
    global __points
    __points -= 10
