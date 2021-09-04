import numpy as np

num_examples = 10
N = 3
to_print = False
for seed in [15]:
    np.random.seed(seed)
    n_accept = 0
    results = []
    if to_print:
        print("<table><tr><td>Decimal Number</td><td>Input</td><td>Result</td></tr>")
    for i in range(num_examples):
        x = np.random.randint(100)
        bstr = format(x, 'b')
        res = "Reject"
        if x%N == 0:
            res = "Accept"
            n_accept += 1
        if to_print:
            print("<tr><td>", x, "</td><td>", bstr, "</td><td>", res, "</td></tr>")
        else:
            print(bstr, end=' ')
    if to_print:
        print("</table>")
