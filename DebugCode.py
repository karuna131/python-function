#1 (semicolon nhi laga tha)

def sum():
    print(12+13)
sum()


#2 (def ki spelling wrong thi)

def welcome():
    print("Welcome to function")
welcome() 


#3 (function last me call hota he)

def isEven():
    if(12%2==0):
        print("Even Number")
    else:
        print("Old Number") 
isEven()


#4 (* lagaya hai)

def geet(*names):
    for name in names:
        print("welcome", name)
geet("rinki","kavi","rohit","chhaya")


#5(age dali hai)

def info(name, age = "20"):
       print(name + " is " + age + " years old")

info("Sonu")
info("Sana", "17")
info("Umesh", "18") 


#6 (one argument is missing)

def studentDetails(name,currentMilestone,mentorName):
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


studentDetails("karuna","loop","Rani") 