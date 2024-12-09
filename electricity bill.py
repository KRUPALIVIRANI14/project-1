print("electricity bill")
units = int(input("enter the units:-"))
if units <= 100:
    x = units*0.5
    print(x)
elif (units > 100) and (units <= 300):
    z= 100*0.5
    x = units-100
    y = x*0.75
    print(z+y)
elif units > 300:
    x = units-300
    y = x*1
    z = 100*0.50
    a = 200*0.75
    b = y+z+a
    print(b)
