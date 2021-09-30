import random

def gameWin(comp,you):
    if (comp==you):
        return None
    elif (comp=='s'):
        if (you=='w'):
            return False
        elif (you=='g'):
            return True
    elif (comp=='w'):
        if (you=='g'):
            return False
        elif (you=='s'):
            return True
    elif (comp=='g'):
        if (you=='s'):
            return False
        elif (you=='w'):
            return True
    

print("Computer turn: Snake(s) water(w) or gun(g)")
c=random.randint(1,3)
if(c==1):
    comp='s'
elif(c==2):
    comp='w'
elif(c==3):
    comp='g'

you=input("Your turn: Snake(s) water(w) or gun(g): ")

print(f"Computer chose {comp}")
print(f"You chose {you}")

w=gameWin(comp,you)
if (w==None):
    print("This is a tie!")
elif w:
    print("You win!")
else:
    print("You lose!")