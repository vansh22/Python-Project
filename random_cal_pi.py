# Q.There is random function which generates a function randomly btw 0 and 1 
# and it is uniformly distributed 
# so calculte the value of pi😂

# import random
# print(random.random())

import random
n=int(input("Enter a number,bigger the number more accurate will be the value of pi:\n"))
# def estimate_pi(n):
number_pt_circle=0
number_pt_total=0
# for _ in range(n):
i=0
for i in range(n):
    x=random.random()
    y=random.random()
    dist=x**2+y**2
    if(dist<=1):
        number_pt_circle+=1
    number_pt_total+=1
print("pi = ",4*number_pt_circle/number_pt_total)   #value of pi
# return 4*number_pt_circle/number_pt_total