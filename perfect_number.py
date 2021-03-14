
n=int(input("Enter a number"))
def perfect(n):
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        print("It is a perfect number")
    else:
        print("It is not a perfect number")
perfect(n)
    