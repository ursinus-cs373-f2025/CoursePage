def halts(func, arg):
    pass # This is our mystery function, which returns True if func(arg) terminates

def weird_opposite(func):
    if halts(func, str(func)):
        return False
    else:
        return True

What does weird_opposite(weird_opposite) do?
