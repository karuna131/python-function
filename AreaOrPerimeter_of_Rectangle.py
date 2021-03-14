#Write a function to calculate area and perimeter of a rectangle.

# l=int(input("Length of rectangle : "))
# w=int(input("Width of rectangle : "))
# area=l*w
# perimeter=2*(l+w)
# print("Area of Rectangle : ",area)
# print("Perimeter of Rectangle : ",perimeter)



#Write a function to calculate area and circumference of a circle.

def area(radius):
    return 2 * radius
def circumference(radius):
    return 2 * math.pi * radius
r=float(input("Enter radius of a circle : "))
Area=area(r)
Circomference=circumference(r)
print("Area of a circle : ",Area)
print("Circomference of a circle : ",Circomference)
