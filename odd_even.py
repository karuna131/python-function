
op_limit=int(input("Enter a limit : "))
def showNumbers(limit):
    while limit<=op_limit:
        if limit%2==0:
            print(limit, "even number")
        else:
            print(limit, "odd number")
        limit+=1
showNumbers(0) 