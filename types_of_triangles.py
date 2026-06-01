# Check if three sides can form a triangle and classify its type
# based on structural properties and angles.

side1 = float(input("Enter size 1: "))
side2 = float(input("Enter size 2: "))
side3 = float(input("Enter size 3: "))
possible = True

# See if the triangle exists
if side1 >= side2 + side3:
    possible = False
elif side2 >= side1 + side3:
    possible = False
elif side3 >= side2 + side1:
    possible = False

if possible == False:
    print("DOES NOT FORM TRIANGLE")

else:
    # See what type of triangle it is by angles
    # Testing all combinations since any side could be the largest
    if (side1*side1 == side2*side2 + side3*side3) or (side2*side2 == side1*side1 + side3*side3) or (side3*side3 == side2*side2 + side1*side1):
        print("RIGHT TRIANGLE")
        
    elif (side1*side1 > side2*side2 + side3*side3) or (side2*side2 > side1*side1 + side3*side3) or (side3*side3 > side2*side2 + side1*side1):
        print("OBTUSE TRIANGLE")
        
    else:
        print("ACUTE TRIANGLE")

    # See what type of triangle it is by sides
    if side1 == side2 == side3:
        print("EQUILATERAL TRIANGLE")
        
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("ISOSCELES TRIANGLE")
        
    else:
        print("SCALENE TRIANGLE")