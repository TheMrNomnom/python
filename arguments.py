# python function arguments

def greet(name, msg = "Good morning!"):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet(name = "Bruce", msg = "How do you do?") # 2 keyword arguments
greet(msg = "How do you do?", name = "Bruce") # 2 kwargs (out of order)

# 1 positional, 1 kwarg
greet("How do you do?", msg = "Bruce")



# arbitrary (unknown number of) arguments
def greet2(*names):
    """This function greets all
    the person in the name tuple"""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

greet2("Monica", "Luke", "Steve", "John")
