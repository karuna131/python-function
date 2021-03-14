def max_func():
    number=[3,5,7,34,2,89,2,5]
    i=0
    greater=number[0]
    while i<len(number):
        if number[i]>greater:
            greater=number[i]
        i+=1
    print(greater)
max_func()