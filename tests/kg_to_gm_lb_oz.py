from tkinter import *

window = Tk()

def kg_to_gm_lb_oz():
    kg = float(e1_value.get())
    gm, lb, oz = kg * 1000, kg * 2.20462, kg * 35.274
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)
    t1.insert(END, gm)
    t2.insert(END, lb)
    t3.insert(END, oz)


l1 =Label(window, text='Kg')
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1 = Button(window, text = 'Convert', command=kg_to_gm_lb_oz)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
