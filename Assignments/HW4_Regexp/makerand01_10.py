import numpy as np

num_examples = 10
to_print = False
for seed in [15]:
    np.random.seed(seed)
    n_accept = 0
    results = []
    if to_print:
        print("<table><tr><td>Input</td><td>01 Count</td><td>10 Count</td><td>Result</td></tr>")
    for i in range(num_examples):
        x = np.random.randint(2**20)
        bstr = format(x, 'b')
        res = "Reject"
        counts01 = 0
        s01 = ""
        i = 0
        while i < len(bstr):
            if bstr[i:i+2] == "01":
                counts01 += 1
                s01 += "<span style=\"color:red\">01</span>"
                i += 2
            else:
                s01 += bstr[i]
                i += 1

        counts10 = 0
        s10 = ""
        i = 0
        while i < len(bstr)-1:
            if bstr[i:i+2] == "10":
                counts10 += 1
                s10 += "<span style=\"color:red\">10</span>"
                i += 2
            else:
                s10 += bstr[i]
                i += 1
        
        if counts01 == counts10:
            res = "Accept"
            n_accept += 1
        if to_print:
            print("<tr><td>", bstr, "</td><td>", s01, " ({})</td><td>".format(counts01), s10, "({})</td><td>".format(counts10), res, "</td></tr>")
        else:
            print(bstr, end=' ')
    if to_print:
        print("</table>")
