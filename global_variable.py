x = "awesome"  # variable declaring outside the function is called global variable


def myfunc():
    print("Python is " + x)


myfunc()


# or we can use global keyword before varible

def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
