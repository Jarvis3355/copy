

import cmath

# Input coefficients
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Calculate the two roots
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

# Print the roots
print("Root 1:", root1)
print("Root 2:", root2)
