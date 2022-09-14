a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))

opr=input("Input Task: ")

if opr=="+":
    print(a+b)
    
elif opr=="-":
    print(a-b)

elif opr=="*":
    print(a*b)

else: print("Operation Not Permitted")