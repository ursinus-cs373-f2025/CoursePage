import re

## Regular expression for problem 5 on HW3
## {A nonzero/even number of a's or a nonzero/even number of b's}
r = "(b*ab*a(b|ab*a)*)" + "|" + "(a*ba*b(a|ba*b)*)"
r = "(" + r + ")"
## followed by {at least one b}
r += "bb*"
## followed by {an odd number of a's or an odd number of b's}
r += "((b*a(b|ab*a)*)|(a*b(a|ba*b)*))"

print(r)
fin = open("tests5.txt")
for s in fin.read().split():
    s = s.strip()
    print(s, re.fullmatch(r, s) is not None)
fin.close()

print("Finished")
