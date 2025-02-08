file = open("Hello.txt", "r")
# a - append, r - read, w - write
# file.write("\nHello Adamson")
numbers = file.readlines()
print(numbers)

file.close()