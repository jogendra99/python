a= int(input("Enter Total no of class held= "))
b= int(input("Enter Total no of class attended= "))
if(b>a):
    print("Attended class cannot be more than class held")
    
elif(b/a*100>=75):
    print("You can attend exam")
else:
    print("Your attend is less to attend the exam")
