from tkinter import *
from tkinter import ttk
from math import *
import tkinter as tk
import sys

calwind=Tk()
calwind.title("Hesap Makinesi")
calwind.geometry("300x300")
calwindfram=Frame(calwind)
calwindfram.grid()

result=0.0


num1str_label = Label(calwindfram, text="Number1: ")
num1str_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

num1str_entry = Entry(calwindfram,bd=2)
num1str_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

num2str_label = Label(calwindfram, text="Number2 :")
num2str_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

num2str_entry = Entry(calwindfram,bd=2)
num2str_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

result_label = Label(calwindfram)
result_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5) 



def sum():
    try:
        num1=float(num1str_entry.get())
        num2=float(num2str_entry.get())
        result_label.config(text=str(num1+num2))
        
    except:
        print("Oops")
        text1=str(sys.exc_info()[0])
        result_label.config(text=text1.split("'")[1])
def sub():
    try:
        num1=float(num1str_entry.get())
        num2=float(num2str_entry.get())
        result_label.config(text=str(num1-num2))
    except:
        print("Oops")
        text1=str(sys.exc_info()[0])
        result_label.config(text=text1.split("'")[1])
def mul():
    try:
        num1=float(num1str_entry.get())
        num2=float(num2str_entry.get())
        result_label.config(text=str(num1*num2))
    except:
        print("Oops")
        text1=str(sys.exc_info()[0])
        result_label.config(text=text1.split("'")[1])
def div():
    try:
        num1=float(num1str_entry.get())
        num2=float(num2str_entry.get())
        result_label.config(text=str(num1/num2))
    except:
        print("Oops")
        text1=str(sys.exc_info()[0])
        result_label.config(text=text1.split("'")[1])
    

buttonsum=Button(calwindfram,text="+",width=5,height=2,command=sum)
buttonsum.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)
buttonsub=Button(calwindfram,text="-",width=5,height=2,command=sub)
buttonsub.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)
buttonmul=Button(calwindfram,text="*",width=5,height=2,command=mul)
buttonmul.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)
buttondiv=Button(calwindfram,text="/",width=5,height=2,command=div)
buttondiv.grid(column=2, row=3, padx=5, pady=5)
buttonexit=Button(calwindfram,text="exit",width=5,height=2,command=lambda:calwind.quit())
buttonexit.grid(column=2, row=4, sticky=tk.W, padx=5, pady=5)

result_label = Label(calwindfram, text="Result :"+str(result))
result_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5) 
print(num1str_entry.get(),num2str_entry.get())
calwind.mainloop()