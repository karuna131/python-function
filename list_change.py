
def list_change(list1,list2):
    i=0
    j=0
    while i<len(list1):
        print(list1[i]*list2[j])
        i+=1
        j+=1
list1=[5, 10, 50, 22]
list2=[2,20,3,5]
multiple_list = list_change(list1,list2)



'''Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke beech ke 
number jo ki 3 aur 5 ke multiples hain unka sum print karega.jaisa ki niche dikhaya gya hai.
3 aur 5 ke multiples => 3, 5, 6, 9, 10'''

number=int(input("Enter a limit"))
def value(limit):
    sum=0
    while limit<=number:
        if limit%3==0 or limit%5==0:
            sum+=limit
            print(limit)
        limit+=1
    print(sum)
value(0)





