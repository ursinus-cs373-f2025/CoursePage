"""
Programmer: Chris Tralie
Purpose: To do the proof by construction that any finite language
of finite strings is regular by constructing a DFA in JFLAP to
recognize it
"""


def write_dfa_jflap(states_pos, transitions, qstart, Final, filename):
    """
    Convert a python dictionary describing DFA transitions into
    XML that JFLAP understands

    Parameters
    ----------
    states_pos: Dictionary: String->(float, float)
        Dictionary of state->(x, y) position of each state
    transitions: Dictionary: String -> (Dictionary: String -> String)
        Dictionary of state->character->next
        For any characters in the alphabet not specified as a transition, assume
        it means go back to the beginning
    qstart: string
        Start state
    Final: list of string
        Accept states
    filename: string
        Path to which to write JFLAP file
    """
    import numpy as np
    BEGIN_JFF = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!--Created automatically by Chris Tralie's finitelang.py-->
    <structure>
    <type>fa</type>
    <automaton>
    """
    ## Step 0: Come up with a unique ID for every state
    IDs = {s:i for i, s in enumerate(states_pos.keys())}

    ## Step 1: Setup the states
    jff_string = "" + BEGIN_JFF
    states_xml = ""
    for state in states_pos.keys():
        d = ""
        if state == qstart:
            d = "<initial/>"
        if state in Final:
            d = "<final/>"
        (x, y) = states_pos[state]
        states_xml += "<state id=\"{}\" name=\"{}\">\n    <x>{}</x>    <y>{}</y>\n{}</state>\n".format(IDs[state], state, x, y, d)
    # Now make the transitions
    jff_string += states_xml
    for state_from in transitions.keys():
        for c, state_to in transitions[state_from].items():
            jff_string += "<transition>\n    <from>{}</from>\n    <to>{}</to>\n    <read>{}</read>\n</transition>\n".format(IDs[state_from], IDs[state_to], c)
    jff_string += "</automaton></structure>"
    fout = open(filename, "w")
    fout.write(jff_string)
    fout.close()

def setup_dfa_states(s, states_pos, transitions, max_depth, width, height, pos=(0, 0)):
    """
    Parameters
    ----------
    s: string
        String being built so far
    states_pos: Dictionary: String->(float, float)
        Dictionary of state->(x, y) position of each state
    transitions: Dictionary: String -> (Dictionary: String -> String)
        Dictionary of state->character->next
        For any characters in the alphabet not specified as a transition, assume
        it means go back to the beginning
    max_depth: int
        Maximum depth of tree
    width: float
        Width of tree 
    height: float
        Height of tree
    pos: (float, float)
        Position of this node
    """
    depth = len(s) # Current depth
    states_pos[s] = pos
    if depth <= max_depth:
        transitions[s] = {"0":s+"0", "1":s+"1"}
        pos_left = (pos[0]-width/2**(depth+1), pos[1] + height/(max_depth+2))
        setup_dfa_states(s+"0", states_pos, transitions, max_depth, width, height, pos_left)
        pos_right = (pos[0]+width/2**(depth+1), pos[1] + height/(max_depth+2))
        setup_dfa_states(s+"1", states_pos, transitions, max_depth, width, height, pos_right)
    else:
        # Setup the "reject state" if we get a string that's too long
        transitions[s] = {"0":"qrej", "1":"qrej"}
        states_pos["qrej"] = (0, height)
        transitions["qrej"] = {"0":"qrej", "1":"qrej"}


def make_dfa_finite_lang(L, width, height):
    """
    Create A DFA that recognizes a finite set of finite strings, using
    the binary tree construction

    Parameters
    ----------
    L: list of string
        Strings in the language

    Returns
    -------
    states_pos: Dictionary: String->(float, float)
        Dictionary of state->(x, y) position of each state
    transitions: Dictionary: String -> (Dictionary: String -> String)
        Dictionary of state->character->next
        For any characters in the alphabet not specified as a transition, assume
        it means go back to the beginning
    qstart: string
        Start state
    Final: list of string
        Accept states
    """
    states_pos = {}
    transitions = {}
    setup_dfa_states("q", states_pos, transitions, max([len(s) for s in L]), width, height)
    return states_pos, transitions, "q", ["q"+s for s in L]


## Example 1: L = {0, 1, 01}
L = ["0", "1", "01"]
states_pos, transitions, qstart, F = make_dfa_finite_lang(L, 400, 200)
write_dfa_jflap(states_pos, transitions, qstart, F, "0_1_01_tree.jflap")

## Example 2: L = {Binary strings s | len(s) <= 5 and s is a palindrome}
def is_palindrome(s):
    res = True
    for i in range(len(s)):
        res = res and s[i] == s[-(1+i)]
    return res

def make_bin_strings(max_digits, L=None, s=""):
    """
    Create a list of binary strings with at most max_digits digits
    """
    if not L:
        L = []
    L.append(s)
    if len(s) < max_digits:
        make_bin_strings(max_digits, L, s+"0")
        make_bin_strings(max_digits, L, s+"1")
    return L

L = [s for s in make_bin_strings(5) if is_palindrome(s)]
states_pos, transitions, qstart, F = make_dfa_finite_lang(L, 1800, 600)
write_dfa_jflap(states_pos, transitions, qstart, F, "palindromes5max.jflap")