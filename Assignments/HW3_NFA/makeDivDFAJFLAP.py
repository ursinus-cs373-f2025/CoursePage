import numpy as np

N = 6

BEGIN_JFF = """<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 6.4.--><structure>
	<type>fa</type>
	<automaton>"""

## Step 1: Forward DFA
# Make the states first
r = 300
s = "" + BEGIN_JFF
states = ""
for i in range(N):
    x = 1.1*r + r*np.cos(np.pi + 2*np.pi*i/N)
    y = 1.1*r + r*np.sin(np.pi + 2*np.pi*i/N)
    d = ""
    if i == 0:
        d = "<initial/><final/>"
    states += "<state id=\"{}\" name=\"q{}\">\n    <x>{}</x>    <y>{}</y>\n{}</state>".format(i, i, x, y, d)
# Now make the transitions
s += states
revtrans = {} # Remember the reverse arrows
for i in range(N):
    for b in range(2):
        to = (2*i + b)%N
        s += "<transition>\n    <from>{}</from>\n    <to>{}</to>\n    <read>{}</read>\n</transition>\n".format(i, to, b)
        if not to in revtrans:
            revtrans[to] = {0:[], 1:[]}
        revtrans[to][b].append(i)
s += "</automaton></structure>"
fout = open("DivDFA.jff", "w")
fout.write(s)
fout.close()

## Step 2: Reverse DFA
s = BEGIN_JFF + states
for frm in revtrans:
    for b in revtrans[frm]:
        for to in revtrans[frm][b]:
            s += "<transition>\n    <from>{}</from>\n    <to>{}</to>\n    <read>{}</read>\n</transition>\n".format(frm, to, b)
s += "</automaton></structure>"
fout = open("DivRevNFA.jff", "w")
fout.write(s)
fout.close()

## Step 3: Create Reverse DFA
states = {} # Set of tuple states
processing = set([ (0,) ]) # States that still need to be processed
finished = set([])
while len(processing) > 0:
    state = processing.pop()
    states[state] = {0:[], 1:[]}
    for b in [0, 1]:
        next = set([])
        # Look at all transitions from all states in the tuple via this bit
        for x in state:
            for y in revtrans[x][b]:
                next.add(y)
        next = tuple(sorted(list(next)))
        states[state][b].append(next)
        if not next in finished:
            processing.add(next)
    finished.add(state)
print(finished)
print(states)

def get_name_str(state):
    name = ""
    for x in state:
        name += "q{},".format(x)
    return name[0:-1]

# Output states
s = "" + BEGIN_JFF
state_to_id = {}
for i, state in enumerate(states):
    state_to_id[state] = i
    x = 1.1*r + r*np.cos(np.pi + 2*np.pi*i/len(states))
    y = 1.1*r + r*np.sin(np.pi + 2*np.pi*i/len(states))
    name = get_name_str(state)
    d = ""
    if state == (0,):
        d = "<initial/>"
    if 0 in state:
        d += "<final/>"
    s += "<state id=\"{}\" name=\"q{}\">\n    <x>{}</x>    <y>{}</y>\n{}</state>".format(i, name, x, y, d)

# Output transitions
for i, state in enumerate(states):
    for b in range(2):
        for next in states[state][b]:
            j = state_to_id[next]
            s += "<transition>\n    <from>{}</from>\n    <to>{}</to>\n    <read>{}</read>\n</transition>\n".format(i, j, b)

s += "</automaton></structure>"
fout = open("DivRevDFA.jff", "w")
fout.write(s)
fout.close()