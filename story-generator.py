#!/usr/bin/env python3

# a python script to generate a random story each time it's run
#
# ********** refine this!! **********
#
# add more options, make the story longer, or make it more like the one at the BYU library where it spits out a short story for real?
# hmmmmm


import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan','Once upon a time','One day']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat','a dog','a horse','a kid','a youngster','a jedi']
name = ['Ali', 'Miriam','Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England','America','Uruguay','Brazil','France','New York City','the country','the big city','the bayou','the suburbs']
went = ['movies','university','seminar', 'school', 'laundramat','museum','market','library','park','bus station','train station']
happened = ['made a lot of friends','ate a burger', 'found a secret key', 'solved a mistery', 'wrote a book','said something silly']

print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + ' lived in ' + random.choice(residence) + ' went to the ' + random.choice(went) + ' and ' + random.choice(happened))
