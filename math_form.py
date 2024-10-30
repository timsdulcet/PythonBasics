import math

# Input the lengths of the two legs
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# Calculate the hypotenuse
c = math.sqrt(a**2 + b**2)

# Output the result
print("The hypotenuse is:", c)
