"""
f = open("test.txt") # opens file in the current directory
f = open("C:/Python38/README.txt") # specifying full path

r = Opens a file for reading (Default)
w = Opens a file for writing. Creates a new file if it does not exist.
x = Opens a file for exclusive creation. If the file already exists,
    this does nothing.
a = Opens a file for appending at the end of the file without truncating it.
    Creates a new file if it does not exist.

t = Opens a file in text mode (Default)
b = Opens a file in binary mode
+ = Opens a file for updating (reading and writing)



# What do these lines do individually?
f = open("test.txt")
f = open("test.txt", 'w')
f = open("img.bmp", "r+b")

# Specify encoding
f = open("test.txt", mode = "r", encoding = "utf-8")

f.close()
"""
with open("test.txt", "w", encoding = "utf-8") as f:
    f.write("my first file\n")
    f.write("This file\n")
    f.write("contains three lines\n")

f.read()
# Outputs "my first file\nThis file\ncontains three lines\n"
