import numpy as np
import random

num_examples = 10
to_print = True
for seed in [0]:
    np.random.seed(seed)
    n_accept = 0
    results = []
    if to_print:
        print("<table style=\"width:200px;\"><tr><td>Input</td><td>Result</td></tr>")
    for i in range(num_examples):
        randlen = np.random.randint(1, 11)
        bstr = ""
        for k in range(randlen):
            bstr += np.random.choice(["a", "b", "c"])
        res = "Reject"
        if "ab" in bstr or "bc" in bstr:
            res = "Accept"
            n_accept += 1
        if to_print:
            print("<tr><td>", bstr, "</td><td>", res, "</td></tr>")
        else:
            print(bstr, end=' ')
    if to_print:
        print("</table>")
