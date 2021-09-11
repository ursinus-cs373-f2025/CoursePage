import numpy as np

np.random.seed(0)
a = "computerscience"
b = "philosophy"

n_examples = 5
print("<ul>")
for i in range(n_examples):
    s = ""
    # Just like merging in merge sort
    i1 = 0
    i2 = 0
    while i1 < len(a) and i2 < len(b):
        i12 = min(len(a), i1+np.random.randint(1, 4))
        i22 = min(len(b), i2+np.random.randint(1, 4))
        s += "<span style=\"color:blue\">" + a[i1:i12] + "</span>"
        s += "<span style=\"color:red\">" + b[i2:i22] + "</span>"
        i1 = i12
        i2 = i22
    while i1 < len(a):
        i12 = min(len(a), i1+np.random.randint(4))
        s += "<span style=\"color:blue\">" + a[i1:i12] + "</span>"
        i1 = i12
    while i2 < len(b):
        i22 = min(len(b), i2+np.random.randint(4))
        s += "<span style=\"color:red\">" + b[i2:i22] + "</span>"
        i2 = i22
    print("    <li>", s, "</li>")
print("</ul>")