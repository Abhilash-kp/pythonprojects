from tkinter import *
import re

i=0
def click(clicked):
    global i
    e.insert(i,clicked)
    i = i + 1

def clear_btn():
    global i
    e.delete(0, END)
    i = 0

def del_btn():
    global i
    e.delete(i-1, END)
    i = i - 1

def eq_btn():
    global i
    exp = e.get()
    e.delete(0,END)
    while "+" in exp or '-' in exp or '*' in exp or '/' in exp:
        if '/' in exp:
            val = re.search(r'(?P<first>\d+\.?\d*)\/(?P<second>\d+\.?\d*)', exp)
            result = float(val.group('first'))/float(val.group('second'))
            exp = re.sub(re.escape(val.group(0)), str(result), exp)
            continue
        if '*' in exp:
            val = re.search(r'(?P<first>\d+\.?\d*)\*(?P<second>\d+\.?\d*)', exp)
            result = float(val.group('first')) * float(val.group('second'))
            exp = re.sub(re.escape(val.group(0)), str(result), exp)
            continue

        if '+' in exp:
            val = re.search(r'(?P<first>\d+\.?\d*)\+(?P<second>\d+\.?\d*)', exp)
            result = float(val.group('first')) + float(val.group('second'))
            exp = re.sub(re.escape(val.group(0)), str(result), exp)
            continue

        if '-' in exp:
            val = re.search(r'(?P<first>\d+\.?\d*)\-(?P<second>\d+\.?\d*)', exp)
            result = float(val.group('first')) - float(val.group('second'))
            exp = re.sub(re.escape(val.group(0)), str(result), exp)
            continue

    e.insert(0,exp)
    i = len(exp)


root = Tk()
root.title('calculator')

e = Entry(root, borderwidth=5)

button_1 = Button(root, text="1",padx=12, pady=12, command= lambda: click(1))
button_2 = Button(root, text="2",padx=12, pady=12, command= lambda: click(2))
button_3 = Button(root, text="3",padx=12, pady=12, command= lambda: click(3))

button_4 = Button(root, text="4",padx=12, pady=12, command= lambda: click(4) )
button_5 = Button(root, text="5",padx=12, pady=12, command= lambda: click(5))
button_6 = Button(root, text="6",padx=12, pady=12, command= lambda: click(6))

button_7 = Button(root, text="7",padx=12, pady=12, command= lambda: click(7))
button_8 = Button(root, text="8",padx=12, pady=12, command= lambda: click(8))
button_9 = Button(root, text="9",padx=12, pady=12, command= lambda: click(9))

button_0 = Button(root, text="0",padx=12, pady=12, command= lambda: click(0))
button_add = Button(root, text="+",padx=12, pady=12, command= lambda: click("+"))
button_sub = Button(root, text="-",padx=12, pady=12, command= lambda: click("-"))

button_mul = Button(root, text="*",padx=12, pady=12, command= lambda: click("*"))
button_div = Button(root, text="/",padx=12, pady=12, command= lambda: click("/"))
button_del = Button(root, text="del",padx=8, pady=10, command=del_btn)
button_clr = Button(root, text="C",padx=12, pady=12, command=clear_btn)
button_equal = Button(root, text="=",padx=25, pady=12, command=eq_btn)


e.grid(row=0, column=0, columnspan=3, pady=10)

button_1.grid(row=3, column=0 )
button_2.grid(row=3, column=1 )
button_3.grid(row=3, column=2 )

button_4.grid(row=2, column=0 )
button_5.grid(row=2, column=1 )
button_6.grid(row=2, column=2 )

button_7.grid(row=1, column=0 )
button_8.grid(row=1, column=1 )
button_9.grid(row=1, column=2 )

button_0.grid(row=4, column=1 )
button_add.grid(row=4, column=0 )
button_sub.grid(row=4, column=2 )

button_mul.grid(row=5, column=0 )
button_div.grid(row=5, column=1 )
button_del.grid(row=5, column=2 )
button_clr.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2 )

root.mainloop()