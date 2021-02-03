a= int(input("A enter first age= "))
b= int(input("B enter second age= "))
c= int(input("C ener third age= "))

if(a>b and b>c):
    print("A is older")
    print("C is younger")
elif(b>a and a>c):
    print("b is older")
    print("c is younger")
elif(c>a and a>b):
    print(" C is older")
    print("B is yunger")
elif(a>c and c>b):
    print("A is older")
    print("B is younger")
