from vacuum import *

def reflex_agent(percept):
    if percept:
        return 'clean'
    else:
        return 'north'

x = 0

def count():
    global x
    x += 1
    return x

print(count())
print(count())


# run(20, 50000, reflex_agent)
