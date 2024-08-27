# calculator in python

def add(n1,n2):
    print(n1+n2)

def sub(n1,n2):
    print(n1-n2)


def div(n1,n2):
    print(n1*n2)


def mult(n1,n2):
    print(n1/n2)



n1 = int(input("Enter 1st : "))
n2 = int(input("Enter 2nd : "))
print("------------------------")
print("1.Addition")
print("2.Substraction")
print("3.Division")
print("4.Multiplication")
print("------------------------")
choice = int(input("Enter : "))

if choice == 1:
    add(n1,n2)

elif choice == 2:
    sub(n1,n2)

elif choice == 3:
    div(n1,n2)

elif choice ==4:
    mult(n1,n2)
    