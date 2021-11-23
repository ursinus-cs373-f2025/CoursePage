## An example of a turing enumerator that enumerates
## strings in lexographic order

def evenzeros_test(s):
    zeros = 0
    for c in s:
        if c == "0":
            zeros += 1
    return zeros%2 == 0


N = 20
s = "0"
k = 1
i = 0
while i < N:
    if evenzeros_test(s):
        print(s)
        i += 1
    b = int(s, 2)
    b += 1
    s2 = format(b, 'b')
    if len(s2) > len(s):
        k += 1
        s = "0"*k
    else:
        s = s2
        if len(s) < k:
            s = "0"*(k-len(s)) + s