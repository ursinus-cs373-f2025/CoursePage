def write_dfa_jflap(delta, filename):
    """
    Programmer: Chris Tralie
    Convert a python dictionary describing DFA transitions into
    XML that JFLAP understands

    Parameters
    ----------
    delta: Dictionary: (String, String) -> String
        Transition function from (state, character) -> state
        NOTE: For any characters in the alphabet not specified as a transition, assume
        it means go back to the beginning
    filename: string
        Path to which to write JFLAP file
    """
    import numpy as np
    BEGIN_JFF = """<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with substring.py in Ursinus College CS 373--><structure>
        <type>fa</type>
        <automaton>"""
    ## Step 1: Setup the states
    jff_string = "" + BEGIN_JFF
    states_xml = ""
    def get_id(s):
        ret = 0
        if s != "start":
            ret = 1+int(s.split("_")[1])
        return ret
    delta_orig = delta
    # Convert to (State):(Character:State)
    delta = {}
    for (state, c), state_to in delta_orig.items():
        if not state in delta:
            delta[state] = {}
        delta[state][c] = state_to
    states = delta.keys()
    ## Step 1b: Setup state positions
    width = 100
    r = len(states)*width/2
    for state in states:
        id = get_id(state)
        d = ""
        if state == "start":
            x = r
            y = r/2
            d = "<initial/>"
        else:
            theta = np.pi*id/len(states)
            x = r - r*np.cos(theta)
            y = -r*np.sin(theta)
        if id == len(states)-1:
            d = "<final/>"
        states_xml += "<state id=\"{}\" name=\"{}\">\n    <x>{}</x>    <y>{}</y>\n{}</state>".format(id, state, x, y, d)
    ## Step 2: Setup the transitions
    jff_string += states_xml
    for state_from in delta.keys():
        state_from_id = get_id(state_from)
        for c in delta[state_from].keys():
            state_to = get_id(delta[state_from][c])
            jff_string += "<transition>\n    <from>{}</from>\n    <to>{}</to>\n    <read>{}</read>\n</transition>\n".format(state_from_id, state_to, c)
    jff_string += "</automaton></structure>"
    fout = open(filename, "w")
    fout.write(jff_string)
    fout.close()

## TODO: Create make_substring_dfa

if __name__ == '__main__':    
    Sigma = ['a', 'b', 'c']
    pattern = "ababac"
    delta = make_substring_dfa(Sigma, "ababac")
    for key, value in delta.items():
        print(key, ":", value)
    write_dfa_jflap(delta, "ababac.jff")
