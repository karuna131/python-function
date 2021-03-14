def menu(day, time):
    if day=="monday":
        if time=="breakfast":
            return "poha"
        elif time=="lunch":
            return "dal chaval"
        elif time=="dinner":
            return "chhola chaval"
        else:
            return "no time is there"
    elif day=="tuesday":
        if time=="breakfast":
            return "bada paw"
        elif time=="lunch":
            return "sabji roti"
        elif time=="dinner":
            return "khir puri"
        else:
            return "no time is there"
    else:
        if time=="breakfast":
            return "upma"
        elif time=="lunch":
            return "rajma chaval"
        elif time=="dinner":
            return "pulav"
        else:
            return "no time is there"
print(menu("monday","lunch"))
print(menu("tuesday","dinner"))