# Coding  in utf-8
"""This function imports a .txt file and shows it at a given words/min.
This idea is used as a programming exercises and is completely based
on the work of Spritz.com"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import button
import chardet
import string

def updatefig(num):
    time_text = ax.text(offsets[num],0,words[num],fontsize = fontsize)
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
    with open(filename,"r",encoding = "utf-8") as inputfile:

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
    .       = 2.00
    ' '     = 2.20
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
    l_0 = 15 # Word length
    l_offset = 3 # offset at legnth = l_0
    k = np.log(l_offset + 1)/l_0
    offset = np.exp(k*x) - 1
    return(offset)

def assign_offsets(wordlist):
    offsetlist = []
    for word in wordlist:
        # [".","!","?",",",";",":","(",")"]
        length = len(word)
        if any([sign in word for sign in string.punctuation]):
            length -= 1
        offset = -0.5*length + offset_func(length)
        # print(word,length,offset)
        offsetlist.append(offset)

    return(offsetlist)


## File
filename = button.select_file("Select .txt file for spritzing")
words = import_words(filename)
offsets = assign_offsets(words)

user_input = button.request_window("Please enter your desired words/minute:")
wpm = int(user_input.result)
times = assign_times(words,wpm)

## Intialize figure
fig = plt.figure(figsize = (10,5), dpi = 80)
ax = fig.add_subplot(111)
xlim = (-10,15)
plt.axis("off")
ax.set_xlim(xlim)
ax.set_ylim(-5,5)



## Calculate fontsize based on dpi and x-axis width to ensure proper shifting
# Get box pixel dimensions
bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
width = bbox.width*fig.dpi

fontsize = (3/2)*width/(xlim[1]-xlim[0])

## Iniialize time_text
time_text = ax.text(0,0,"",)

## Start animation engine
anim = animation.FuncAnimation(fig, updatefig, frames=len(words)-1,blit = True)
plt.show()
