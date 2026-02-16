# count from 1 to 5 using a while loop

i = 1
while i <= 5:
    print(i)
    i += 1



# sum of numbers from 1 to 10 using a while loop

total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Sum =", total)



# Never ending loop until user types 'quit'

command = ""
while command != "quit":
    command = input("Type 'quit' to exit: ")
print("Exited the loop")



# keep doubling a number

num = 1
while num <= 100:
    print(num)
    num *= 2



# guessing game

secret_number = 7 
guess = 0
while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")

