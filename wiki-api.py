# a Python script that prompts the user for a topic and gives the user options for what to learn about the topic
# by Stevie Bird
# ****** work in progress! moving on to a more advanced application of Python... ******

# ---------------- setup ----------------
# (should this be in a setup.py file? how does that work to put the python files into a package? do some research here, it feels important

import pkg_resources
import subprocess
import sys
import os

REQUIRED = {
  'wikipedia'
}

installed = {pkg.key for pkg in pkg_resources.working_set}
missing = REQUIRED - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
   
# ---------------- end setup ----------------
  
# display an intro to the user (directions)

# what user input is expected? initialize any variables that need initial values then prompt for input
term = input('What would you like to learn about? ')

# first search wikipedia for possible terms (if there are too many options it will throw an error) and ask the user which term they want info on
# present the first 10 options
term_list = wikipedia.search(term, results=10)

# print a list of the terms for the user to choose one  
i = len(term_list)  # get the number of returned search terms 
for x in range(i):
    print(x, term_list[x])
t = input('Which term best describes what you would like to learn about? ') 
term = term_list[t]

# get wikipedia data
w = wikipedia.page(term)

# present wikipedia data to user
print('\n')
print(f'{term} - Wikipedia entry for', w.title)
print('\n')
print(w.content)
print('\n')
print('Source:', w.url) 
          

# wikipedia options:
# related terms
# print(wikipedia.search("Python"))
# topic summary
# print(wikipedia.summary("Python"))
# others:
# wikipedia.set_lang("en")
# p = wikipedia.page("Python")
# print(p.title)
# print(p.url)
# print(p.content)
# print(p.images)
# print(p.links)
