import numpy as np
from fractions import Fraction

allnums = {}
nums = {}
decnums = set([])

xs = []
NZigzags = 45
a = 1
b = 1
for i in range(NZigzags):
    if a == 0:
        a = b
        b = 1
    if not a/b in decnums:
        decnums.add(a/b)
        nums[(a, b)] = len(nums)+1
    allnums[(a, b)] = len(allnums)
    a -= 1
    b += 1



M = np.max([n[0] for n in nums.keys()] + [n[1] for n in nums.keys()])


fout = open("zigzagrational.js", "w")
fout.write("let zigzag = {};\n")
fout.write("let zigzagdesc = {};\n")
for i in range(NZigzags):
    s = "<table><tr><td></td>"
    for b in range(1, M+1):
        s += "<td>b = {}</td>".format(b)
    s += "</tr>"
    desc = ""
    for a in range(1, M+1):
        s += "<tr><td>a = {}</td>".format(a)
        for b in range(1, M+1):
            if not (a, b) in allnums or allnums[(a, b)] > i:
                s += "<td>...</td>"
            else:
                color = 'black'
                xbeg = ""
                xend = ""
                if (a, b) in nums:
                    color = 'red'
                    xbeg = "({},".format(nums[(a, b)])
                    xend = ")"
                    if allnums[(a, b)] == i+1:
                        desc = "({}, ({}, {}))".format(nums[(a, b)], a, b)
                elif allnums[(a, b)] == i+1:
                    f = Fraction(a, b)
                    desc = "{}/{} has already been assigned!".format(f.numerator, f.denominator)
                s += "<td style=\\\"color: {};\\\">{}{}/{}{}</td>".format(color, xbeg, a, b, xend)
        s += "</tr>"
    s += "</table>"
    fout.write("zigzag[{}] = \"{}\";\n\n".format(i,s))
    fout.write("zigzagdesc[{}] = \"{}\";\n\n".format(i, desc))
fout.write("let NZigzags = {};\n".format(NZigzags))
fout.close()
