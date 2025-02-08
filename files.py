file = open("Hello.txt", "r")
# a - append, r - read, w - write
# file.write("\nHello Adamson")
numbers = file.readlines()
for number in numbers:
    print(number.strip())

file.close()