def write_dfa_jflap(transitions, filename):
    """
    Programmer: Chris Tralie
    Convert a python dictionary describing DFA transitions into
    XML that JFLAP understands

    Parameters
    ----------
    transitions: Dictionary: String -> (Dictionary: String -> String)
        Dictionary of state->character->next
        For any characters in the alphabet not specified as a transition, assume
        it means go back to the beginning
    filename: string
        Path to which to write JFLAP file
    """
    import numpy as np
    BEGIN_JFF = """<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 6.4.--><structure>
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
    states = transitions.keys()
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
    # Now make the transitions
    jff_string += states_xml
    for state_from in transitions.keys():
        state_from_id = get_id(state_from)
        for c in transitions[state_from].keys():
            state_to = get_id(transitions[state_from][c])
            jff_string += "<transition>\n    <from>{}</from>\n    <to>{}</to>\n    <read>{}</read>\n</transition>\n".format(state_from_id, state_to, c)
    jff_string += "</automaton></structure>"
    fout = open(filename, "w")
    fout.write(jff_string)
    fout.close()

def naive_substring_search(pattern, s):
    """
    Implement the naive O(len(pattern) * len(s)) algorithm for finding
    all instances of pattern in s

    Parameters
    ----------
    pattern: string
        Search pattern
    s: string
        String in which to search for pattern
    
    Returns
    -------
    list of int:
        A list of all of the indices at which pattern exists in s
    """
    instances = []
    for i in range(len(s)-len(pattern)+1):
        j = 0
        valid = True
        while valid and j < len(pattern):
            if pattern[j] == s[i+j]:
                j += 1 # Continue along as long as we do match
            else:
                valid = False # Break out early as soon as we don't match
        if valid:
            instances.append(i)
    return instances

## TODO: Create make_substring_dfa

if __name__ == '__main__':    
    Sigma = ['a', 'b', 'c']
    pattern = "ababac"
    transitions = make_substring_dfa(Sigma, "ababac")
    write_dfa_jflap(transitions, "ababac.jff")