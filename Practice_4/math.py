import math

# 1. Degrees to Radians
degree = float(input("Input degree: "))
radian = math.radians(degree)
print(f"Output radian: {radian:.6f}")

# 2. Area of Trapezoid
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = ((base1 + base2) / 2) * height
print(f"Expected Output: {area}")

# 3. Area of Regular Polygon
n = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))
area = (n * side ** 2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area:.0f}")

# 4. Area of Parallelogram
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print(f"Expected Output: {area}")