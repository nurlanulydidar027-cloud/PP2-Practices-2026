# boolean basic

a = True
b = False

print("a =", a)
print("b =", b)

# data type
print(type(a))



# boolean compare

x = 10
y = 5

print(x > y)   # True
print(x < y)   # False
print(x == y)  # False
print(x != y)  # True



# boolean if

is_raining = True

if is_raining:
    print("Take umbrella ☔")
else:
    print("Go outside and enjoy the sun ☀️")



# boolean input

num = int(input("Enter number: "))

is_even = (num % 2 == 0)

print("Is even:", is_even) # True if even, False if odd



# bool() function 

x = "Hello"
y = 15
z = 0

print(bool(x))
print(bool(y))
print(bool(z))