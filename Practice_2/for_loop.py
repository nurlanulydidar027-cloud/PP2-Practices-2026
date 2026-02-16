# Output numbers from 0 to 4 using a for loop

for i in range(5):
    print(i)



# sum of numbers from 1 to 10 using a for loop

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total) 



# run through a list

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("I like", fruit)



# output even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)



# iterate through each letter in a string

word = "python"

for letter in word:
    print(letter)
