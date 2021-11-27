import numpy as np

np.random.seed(0)
sout = "<table><tr><td></td>"
N = 10
for i in range(N):
    sout += "<td>j = {}</td>".format(i+1)
sout == "<td>...</td>"
sout += "</tr>"
alls = []
for i in range(N):
    s = []
    sout += "<tr><td>i = {}</td>".format(i+1)
    for j, b in enumerate(np.random.randint(0, 2, N)):
        s.append(b)
        if i == j:
            sout += "<td style=\"color:red;\">{}</td>".format(b)
        else:
            sout += "<td>{}</td>".format(b)
    alls.append(s)
    sout += "<td>...</td></tr>"
sout += "<tr>"
for j in range(N+2):
    sout += "<td>...</td>"
sout += "</tr></table>"
print(sout)

for i in range(N):
    print(alls[i][i], end='')
print("\n\n")
for i in range(N):
    print(1-alls[i][i], end='')