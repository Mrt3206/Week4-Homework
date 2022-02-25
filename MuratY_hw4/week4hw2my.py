from random import randint
import tkinter as tk

LENGTH=10
MIN_ASCII=33
MAX_ASCII=126


def random_passwd():
    result=""
    alpha=0
    num=0
    spec=0
    flag=True
    while flag:
        for i in range(LENGTH):
            randomChar=chr(randint(MIN_ASCII,MAX_ASCII))
            result=result+randomChar
        result=result.upper()
        for ch in result:
            if ch>="A" and ch<="Z":
                alpha+=1
            elif ch>="0" and ch<="9":
                num+=1
            else:
                spec+=1
        if alpha>=2 and num>=2 and spec>=2:
            label.config(text=result)
            flag=False
        else:
            result=""
            flag=True
            
            
    
        
    
window = tk.Tk()

window.title("Random Password")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Random Password:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to make a password ", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" CHOOSE ", width=50, height=5, command=random_passwd)
button1.grid(padx=110, pady=40)

window.mainloop()
