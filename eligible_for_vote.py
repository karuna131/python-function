user=int(input("Enter age : "))
def eligible_for_vote(user):
    if user<18:
        print("not eligible")
    else:
        print("you are eligible")
eligible_for_vote(user)