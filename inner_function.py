#1

def f1():
    s = "I Love Navgurukul"
    def f2():
        print(s)
    f2()
f1() 


#2
def first_function():
    s = 'I love India'
    def second_function():
        print(s)     
    second_function()
first_function() 


#3
def first_function():
    s = 'I love India'

    def second_function():
        s = "MY NAME IS JACK"
        print(s)     
    second_function()
    print(s)    

first_function() 