x=int(input("number 1(x)"))
y=int(input("number 2(y)"))
z=int(input("number 3(z)"))
if x>y and x>z:
    print("x is the biggest number")
elif y>z and y>x:
    print("y is the biggest number")
elif z>x and z>y:
    print("z is the biggest number")
else:
    print("2 numbers or all three are equal")
