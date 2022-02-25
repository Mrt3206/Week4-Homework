import random
from random import randint
from datetime import datetime
from math import ceil

n=int(input("Range first: "))
m=int(input("Range Last: "))

comp_choice=random.randint(n,m)
flag1=True
flag2=True
guess_num=0
an=datetime.now()

use_choice=int(input("Your choice: "))
begintime=60*an.hour+60*an.minute+an.second

while flag2:
    if comp_choice==use_choice:
        an=datetime.now()
        endtime=60*an.hour+60*an.minute+an.second
        seconds=endtime-begintime
        hours=int(seconds/3600)
        seconds=seconds%3600
        minutes=int(seconds/60)
        seconds=seconds%60
        print(f"Your Total finding Time: {hours} h {minutes} m {seconds} s")
        print(f"Your Total guess time: {guess_num}")
        flag2=False
        break
    elif abs(comp_choice-use_choice)>(comp_choice/10):
        if comp_choice-use_choice >0:
            print("Your choice too low")
            guess_num+=1
            use_choice=int(input("Your choice: "))
            
        elif comp_choice-use_choice<0:
            print("Your choice too high")
            guess_num+=1
            use_choice=int(input("Your choice: "))
            
    else:
            print("Try a better choice")
            guess_num+=1
            use_choice=int(input("Your choice: "))
input()
           
