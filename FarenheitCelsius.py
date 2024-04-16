unknown=input("What do you need to convert into?(Farenheit or Celsius)")
if unknown=="Celsius":
    f=int(input("Enter the temperature in F°:"))
    c=(f-32)*5/9
    print("The temperature in °C is ",c)
else:
    c=int(input("Enter the temperature in °C:"))
    f=(c*9/5)+32
    print("The temperature in °F is ",f)


