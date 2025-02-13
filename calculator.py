def add(Number1,Number2):
    return Number1 + Number2
def sub(Number1,Number2):
    return Number1 - Number2
def mult(Number1,Number2):
    return Number1 * Number2
def div(Number1,Number2):
    return Number1 / Number2
while True: 
    print("\nPlease Select Operation: \n1.Addition \n2.Subtraction \n3.Multiplictaion \n4.division \n5.Exit")
    operation = int(input("Select the Operation among 1,2,3,4,5:"))
    if operation == 5:
        break
    Number1=int(input("Enter First Number:"))
    Number2=int(input("Enter second Number:"))
    if operation == 1:
        print(Number1,"+",Number2,"=",add(Number1,Number2))
    elif operation == 2:
        print(Number1,"-",Number2,"=",sub(Number1,Number2))
    elif operation == 3:
        print(Number1,"*",Number2,"=",mult(Number1,Number2))
    elif operation == 4:
        print(Number1,"/",Number2,"=",div(Number1,Number2))
    else:
        print("Invalid operation")
   