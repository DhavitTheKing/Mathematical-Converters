unknown=input("What do you need to find? (Perimeter or Area)")
if unknown=="Perimeter":
    unknown_2=input("Which shape's perimeter/circumfrence do you need to find? (Square, Circle, Triangle or Rectangle)")
    if unknown_2=="Square":
        side=float(input("Enter your side length:"))
        s_perimeter=side*4
        print("The perimeter of the square is ",s_perimeter)
    elif unknown_2=="Circle":
        radius=float(input("Enter the radius of the circle:"))
        circ=(3.14*2)*radius
        print("The circumfrence of the circle is ",circ)
    elif unknown_2=="Triangle":
        s1=float(input("Enter the length of the first side:"))
        s2=float(input("Enter the length of the second side:"))
        s3=float(input("Enter the length of the third side:"))
        peri=s1+s2+s3
        print("The perimeter of the triangle is ",peri)
    else:
        length=float(input("Enter your length:"))
        breadth=float(input("Enter your breadth:"))
        lb=length+breadth
        r_perimeter=2*lb
        print("The perimet of the rectangle is ",r_perimeter)        
else:
    unknown_3=input("Which shape's area do you need to find? (Square, Circle, Triangle or Rectangle)")
    if unknown_3=="Square":
        side=float(input("Enter your side length:"))
        s_area=side*side
        print("The area of the square is ",s_area)
    elif unknown_3=="Circle":
        r=float(input("Enter the radius of the circle:"))
        c_area=(r*r)*3.14
        print("The area of the circle is ",c_area)
    elif unknown_3=="Triangle":
        h=float(input("Enter the height of the triangle:"))
        base=float(input("Enter the base of the triangle:"))
        t_area=(h*base)*1/2
        print("The area of the triangle is ",t_area)
    else:
        l=float(input("Enter the length of the rectangle:"))
        b=float(input("Enter the breadth of the rectangle:"))
        r_area=l*b
        print("The area of the rectangle is ",r_area)
        
