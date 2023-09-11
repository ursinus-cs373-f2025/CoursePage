import numpy as np
import random

num_examples = 10
to_print = True
strings = []
for seed in [0]:
    np.random.seed(seed)
    n_accept = 0
    results = []
    if to_print:
        print("<table style=\"width:200px;\"><tr><td>Decimal Number</td><td>Input</td><td>Result</td></tr>")
    for i in range(num_examples):
        x = np.random.randint(100)
        bstr = bin(x)[2::]
        strings.append(bstr)
        res = "Reject"
        if x % 4 == 0 or x % 3 == 0:
            res = "Accept"
            n_accept += 1
        if to_print:
            print("<tr><td>", x, "</td><td>", bstr, "</td><td>", res, "</td></tr>")
        else:
            print(bstr, end=' ')
    if to_print:
        print("</table>")
        
print(*strings)
