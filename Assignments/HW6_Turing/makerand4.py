import numpy as np

num_examples = 10
N = 5
print_html = True
results = []

seed = 881
np.random.seed(seed)
s = ""
#s += "<h2>{}</h2>".format(seed)
s += "<table><tr><td>Input</td><td>Result</td></tr>\n"
for i in range(num_examples):
    n_bits = np.random.randint(2, 10)
    X = np.random.randint(2**n_bits)
    n_bits2 = np.random.randint(2, 10)
    Y = np.random.randint(2**n_bits)
    Z = X + Y
    res = "Accept"
    if np.random.rand() < 0.5:
        res = "Reject"
        # Make incorrect
        n_bits = max(n_bits, n_bits2)
        Z += (np.random.randint(2**n_bits-1) + 1) % (2**(n_bits+1))
    X = format(X, 'b')
    Y = format(Y, 'b')
    Z = format(Z, 'b')
    bstr = "".join(Z) + "=" + "".join(X) + "+" + "".join(Y)
    s += "<tr><td>" + bstr + "</td><td>" + res + "</td></tr>\n"
    if not print_html:
        print(bstr, end=' ')
s += "</table>\n"
if print_html:
    print(s)