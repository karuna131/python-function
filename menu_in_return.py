def menu(day):
    if day=="monday":
        return "dal chaval"
    elif day=="tuesday":
        return "roti sabji"
    else:
        return "chhole bhature"
    print("kya ye print hoga")
    #nhi
mon_menu=menu("monday")
print(mon_menu)
tue_menu=menu("tuesday")
print(tue_menu)
fri_menu=menu("friday")
print(fri_menu)