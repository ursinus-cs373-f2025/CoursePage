import numpy as np

num_examples = 10
N = 5
print_html = False
results = []

seed = 0
np.random.seed(seed)
s = ""
#s += "<h2>{}</h2>".format(seed)
s += "<table><tr><td>Input</td><td>Result</td></tr>\n"
for i in range(num_examples):
    n_bits = np.random.randint(2, 10)
    arr = ["0"]*(2*n_bits) + ["1"]*n_bits
    res = "Accept"
    if np.random.rand() < 0.5:
        res = "Reject"
        # Make incorrect
        arr += np.random.choice(["0", "1"])*np.random.randint(1, 10)
    bstr = "".join([arr[k] for k in np.random.permutation(len(arr))])
    s += "<tr><td>" + bstr + "</td><td>" + res + "</td></tr>\n"
    if not print_html:
        print(bstr, end=' ')
s += "</table>\n"
if print_html:
    print(s)