driver=int(input("Enter speed : "))
def car(speed):
    if driver<=speed:
        print("ok")
    elif driver>speed:
        a=driver-speed
        b=a//5
        if b>12:
            print("License suspended")
        else:
            print("you get ",b,"point")
car(70)