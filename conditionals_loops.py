#if-else Statement
# age = 23
# if age > 20:
#     print("You are older than 20")
# else: 
#     print("You are younger than 20")
# num = 0

#Looping Statement

# while num < 10:
#     print(num)
#     num = num + 1

# for num in range(10):
#     print(num)

#Guessing game

secret_number = 4

guess = int(input("Enter your guess: "))

while guess != secret_number:
    if guess < secret_number:
        print("Guess too low")
    else:
        print ("Guess too high")
    guess = int(input("Enter your guess: "))

print("Congratulations you have won") 
