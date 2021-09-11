import numpy as np

divisor = 6
num_examples = 10
to_print = False
for seed in [22]:
    np.random.seed(seed)
    n_accept = 0
    results = []
    if to_print:
        print("<table style=\"width:200px;\"><tr><td>Input</td><td>Decimal Number</td><td>Reverse Binary</td><td>Reverse Decimal</td><td>Result</td></tr>")
    for i in range(num_examples):
        x = np.random.randint(256)
        bstr = format(x, 'b')
        xrev = int(bstr[::-1], 2)
        res = "Reject"
        if x%divisor == 0:
            res = "Accept"
            n_accept += 1
        if to_print:
            print("<tr><td><b>", bstr[::-1], "</b></td><td>", xrev, "</td><td>", bstr, "</td><td>", x, "</td><td><b>", res, "</b></td></tr>")
        else:
            print(bstr[::-1], end=' ')
    if to_print:
        print("</table>")
    #if n_accept > 4:
    #    print(seed, n_accept)
