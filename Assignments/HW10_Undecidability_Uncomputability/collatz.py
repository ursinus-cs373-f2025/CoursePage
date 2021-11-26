def f(x):
    if x%2 == 0:
        return int(x/2)
    return 3*x+1

ns = [11, 13, 111, 174, 373, 2021]
print("""<html>
<head>
    <link rel="stylesheet" href="../../assets/css/main.css" />
</head>   """)
print("<body><table><tr>")
for n in ns:
    print("<td><h3>{}</h3></td>".format(n))
print("</tr><tr>")
for n in ns:
    print("<td><ul>")
    while n != 1:
        n2 = f(n)
        print("<li>f({}) = {}</li>".format(n, n2))
        n = n2
    print("</ul></td>")
print("</tr></table></body></html>")