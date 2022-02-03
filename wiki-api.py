#!/usr/bin/env python3

# a Python script that prompts the user for a topic and gives the user options for what to learn about the topic
# by Stevie Bird
# ****** work in progress! moving on to a more advanced application of Python... ******

# ---------------- setup ----------------
# should this be in a setup.py file? hmm I think that would only be necessary for long programs... here is a good tutorial https://www.teclado.com/30-days-of-python/python-30-day-21-multiple-files

# this uses the wikipedia API 

try:
    import wikipedia 
except: 
    print('\nWikipedia API is not installed. Try again after installing the wikipedia API using the following command: \npython3 -m pip install wikipedia\n')
    # raise ValueError("Type an error to display here") # would this stop running the script and display the error??
    quit() # stop running the script

# ---------------- end setup ----------------
  

# display an intro to the user (directions)??
# what user input is expected? initialize any variables that need initial values then prompt for input
term = input('What would you like to learn about? ')

# first search wikipedia for possible terms (if there are too many options it will throw an error) and ask the user which term they want info on
# present the first 10 options
term_list = wikipedia.search(term, results=10)

# print a list of the terms for the user to choose one 
print('Here are some options:\n') 
i = len(term_list)  # get the number of returned search terms 
for x in range(i):
    print(x, term_list[x])
t = int(input('Which term best describes what you would like to learn about? ')) 
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
          
# if I want to make this a little more complicated....
#
# wikipedia options:
#
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
