#program to display the Fibonacci series using generators.

num=int(input("Enter a number: "))
n1,n2 = 0,1
sum=0
if num<=0:
    print("The number should be greater than 0")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2
    print("\nThis is a fibonacii series: ")

