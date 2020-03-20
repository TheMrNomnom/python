print("Syntax: Syntax is essentially the ‘spelling and grammar’ of computer programming languages.  Just as it may be difficult to understand an English sentence without proper spelling and grammar, a computer can’t understand their commands unless they are laid out properly. Syntax defines the proper way to lay out commands in programming languages.\n")
print("Variables: In computer programming, a variable is a type of value that can change.\n")
print("Loops: Loops contain a set of instructions that are continually repeated until a specific set of conditions are met.\n")

for x in range(1,6):
   print (x)
# range is a method. A method is just a name for a Python command.
print("In a for loop, the computer executes the command for a fixed number of times. In our case, this is defined by the range.\n")

for x in range(6,1,-1):
   print (x)

for x in range(5,0,-1):
  print (x, 'little monkeys jumping on the bed, 1 fell off and bumped his head, momma called the doctor and the doctor said, no more monkeys jumping on the bed')

# Unlike for loops, which typically stop after a fixed number of times, while loops will stop only when a specific condition is met.

x=0
while x is not 10:
    x=x+1
    print (x)
print('done!')

# The library is random, and the method we are taking from it is randint. random is a type of module in Python that gives us several functions available for use.

from random import randint
x = randint(1,4)
print("dice roll:")
print(x)

print(".randint(x, y) is a type of function available through random. This function takes two parameters (two variablesx and y), it will select a random number between x and y, including x and y.  You can set x and y to whatever numbers you like. In this example, we chose 1,6, just like a dice!")

# modifications that can be made, such as changing the minimum and maximum of the numbers that can be produced or deciding to only roll again if the number is less than or equal to five.

from random import randint
roll=randint(1, 6)
print(roll)
if roll < 5 :
    repeat=roll
    print(roll)
else:
    print("You lose")

# Lists are very easy to create in Python.  We simply put a series of comma-separated items between square brackets. We can create a list of words by typing in the following:
myList = ['I', "don’t", "like", "pickles", "in","my", "sandwiches"]
# This action is called declaration in programming; we have just declared the myList variable. This list stores a set of words. The two square brackets are important to define the list.  We can use commands to access information about the list and to edit the data in the list.


print(len("Hello, my name is Aditya."))

variable = len("Cool story bro")
