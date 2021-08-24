# a Python chatbot
# this is a simple rule-based chatbot
# and it needs to be tested and debugged...

# ---- install dependencies? still learning how to do this and this is not the way... ----
# Install NLTK: run pip install --user -U nltk
    
# ---------------- setup ----------------
# (should this be in a setup.py file? how does that work to put the python files into a package? do some research here, it feels important

import pkg_resources
import subprocess
import sys
import os

REQUIRED = {
  'nltk'
}

installed = {pkg.key for pkg in pkg_resources.working_set}
missing = REQUIRED - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
   
# ---------------- end setup ----------------
# ---- finished installing dependencies... or not since this probably didn't work...  ----

from nltk.chat.util import Chat, reflections # import chatbot libraries

# create a variable called 'pairs' that is a list of patterns and responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, how are you today?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name?",
        ["My name is Number 5, but you can just call me Dude and I'm a chatbot.",]
    ],
    [
        r"how are you (.*)?",
        ["I'm doing very well.", "I am great!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.","It's OK, never mind that.","No problem.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that.","Alright, great!",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello.", "Hey there.", "Nice to chat.",]
    ],
    [
        r"what (.*) want?",
        ["Make me an offer I can't refuse.",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health. My master takes care of me.",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Ice Hockey.",]
    ],
    [
        r"who (.*) (hockey|player|goalie)?",
        ["I'm a fan of Claude Giroux, but Dominik Hasek will always be my favorite goalie.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)",]
    ],
    [
        r"(.*)",
        ['That is nice to hear.',]
    ],
]

# this is what is in the included reflections dictionary
# {'i am': 'you are',
# 'i was': 'you were',
# 'i': 'you',
# "i'm": 'you are',
# "i'd": 'you would',
# "i've": 'you have',
# "i'll": 'you will',
# 'my': 'your',
# 'you are': 'I am',
# 'you were': 'I was',
# "you've": 'I have',
# "you'll": 'I will',
# 'your': 'my',
# 'yours': 'mine',
# 'you': 'me',
# 'me': 'you'}

# if I want to create my own reflections dictionary? 
my_own_reflections= {
    'go'     : 'gone',
    'hello'    : 'hey there',
    'i am': 'you are',
    'i was': 'you were',
    'i': 'you',
    "i'm": 'you are',
    "i'd": 'you would',
    "i've": 'you have',
    "i'll": 'you will',
    'my': 'your',
    'you are': 'I am',
    'you were': 'I was',
    "you've": 'I have',
    "you'll": 'I will',
    'your': 'my',
    'yours': 'mine',
    'you': 'me',
    'me': 'you'
}

#default message at the start of chat
print("Hi, I'm Number 5 and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, my_own_reflections)

#Start conversation
chat.converse()
