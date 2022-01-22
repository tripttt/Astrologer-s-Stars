num1 = int(input("Enter the number of rows you want to print:- "))
num2 = int(input("Enter 0 or 1:- "))
bool1 = bool(num2)
if num2 <= 0:
    bool1 == False
if bool1 == False:
    for i in range (num1,0,-1):
        for j in range (i,0,-1):
            print("*", end="")
        print()

if num2 >= 1:
    bool1 == True
if bool1 == True:
    for i in range (1,num1+1):
        for j in range (1,i+1):
            print("*", end="")
        print()
