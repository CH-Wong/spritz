# Coding  in utf-8
"""This function imports a .txt file and shows it at a given words/min.
This idea is used as a programming exercises and is completely based
on the work of Spritz.com"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import button

def updatefig(num):
    time_text = ax.text(offsets[num],0,words[num],fontsize = 50)
    anim.event_source.interval = times[num]
    return time_text,

def import_words(filename):
    """Imports words from a given .txt file and returns it.
    """

    # Initialize resuts variable
    results = []

    # This with statement ensures the file is only open for a certain amount of time.
    # This can save RAM and processing speeds in larger projects
    # Rename the sprits.txt as inputfile within this with statement
    with open(filename) as inputfile:

        # Loop through each line in the defined inputfile variable
        for line in inputfile:

            # Create a new list from each line, and split it at each space " "
            for word in line.strip().split(" "):

                # Individually append every word to the results variable
                results.append(word)
    return(results)


def assign_times(wordlist,speed):
    """Converts word list to a wait_time list to be used as timing variable.b
    Returns a list of timings in seconds. Uses the speed variable to assign
    the desired words/min.
    .       = 1.10
    ' '     = 1.50
    word    = 1.00
    """

    time_list = []

    # Loop through all words in given wordslist
    for word in wordlist:
        if any([stop in word for stop in [".","!","?"]]):
            wait_time = 2.0
        elif any([sign in word for sign in [",",";",":"]]):
            wait_time = 2.2
        else:
            wait_time = 1.0

        time_list.append(wait_time*1000/(speed/60))

    return(time_list)

def offset_func(x):
    max_offset = 2
    x_half = 4
    offset = -max_offset/(1+np.exp(-(x-x_half)))
    return(offset)

def assign_offsets(wordlist):
    offsetlist = []
    for word in wordlist:

        length = len(word)
        if any([sign in word for sign in [".","!","?",",",";",":"]]):
            length -= 1

        offset = offset_func(length)
        offsetlist.append(offset)

    return(offsetlist)


message = "Please enter your desired words/minute:"
user_input = button.request_window(message)
wpm = int(user_input.result)


words = import_words("datafiles/lorem.txt")
times = assign_times(words,wpm)
offsets = assign_offsets(words)


fig = plt.figure(figsize = (10,10), dpi = 80)
ax = fig.add_subplot(111)
plt.axis("off")
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
time_text = ax.text(0,0,"")

anim = animation.FuncAnimation(fig, updatefig, frames=len(words)-1,blit = True)
plt.show()
