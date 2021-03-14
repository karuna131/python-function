#1

def func(name, position):
    print("Mera naam", name," hai.""Main NavGurukul ka", position, "hun.")
func("Rishabh","co-Founder")


#2

def student(*listOfStudent):
    print(listOfStudent)
student("karuna","chhaya","saloni","yogita","nikita")

#3

def isGreaterThen20(first, second="20"):
    print(first, second)
isGreaterThen20(30,"kavi")
isGreaterThen20("kiran")

#4(1)

def add_number(number1,number2):
    print(number1+number2)
num1=56
num2=12
add_number(num1,num2)


#4(2)

def add_numbers_list(number1,number2):
    i=0
    j=0
    while i<len(num1):
        print(number1[i]+number2[j])
        i+=1
        j+=1
num1=[50,60,10]
num2=[10,20,13]
add_numbers_list(num1,num2)


#5(1)

def check_number(number1,number2):
    if number1%2==0 and number2%2==0:
        print("both are even")
    else:
        print("both are not even")
num1=4
num2=6
check_number(num1,num2)


#5(2)

def check_numbers_list(number1,number2):
    i=0
    j=0
    while i<len(num1):
        if number1[i]%2==0 and number2[j]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i+=1
        j+=1
num1=[2, 6, 18, 10, 3, 75]
num2=[6, 19, 24, 12, 3, 87]
check_numbers_list(num1,num2)



#6

def employee(name,salary=20000):
        print(name,"your salary is:-",salary)

employee("kartik",30000)
employee("deepak") 


#7

def primeorNot(num):     
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")

    else:
        print(num,"is not a prime number")
primeorNot(406) 



#8

def greet(*names):
    for name in names:
        print("Hello", name)
greet("sonu", "kartik", "umesh", "bijender")
 

#9

def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number/=10
        return sum

print(sumofdigits(123))
 