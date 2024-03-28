unknown=input("What do you need to find? (Perimeter or Area)")
if unknown=="Perimeter":
    unknown_2=input("Which shape's perimeter do you need to find? (Square or Rectangle)")
    if unknown_2=="Square":
        side=float(input("Enter your side length:"))
        s_perimeter=side*4
        print("The perimeter of the square is ",s_perimeter)
    else:
        length=float(input("Enter your length:"))
        breadth=float(input("Enter your breadth:"))
        lb=length+breadth
        r_perimeter=2*lb
        print("The perimet of the rectangle is ",r_perimeter)        
else:
    unknown_3=input("Which shape's area do you need to find? (Square or Rectangle)")
    if unknown_3=="Square":
        side=float(input("Enter your side length:"))
        s_area=side*side
        print("The area of the square is ",s_area)
    else:
        l=float(input("Enter the length of the rectangle:"))
        b=float(input("Enter the breadth of the rectangle:"))
        r_area=l*b
        print("The area of the rectangle is ",r_area)
        
