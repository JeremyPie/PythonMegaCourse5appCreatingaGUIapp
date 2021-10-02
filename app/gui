from tkinter import *

window = Tk()

l1 = Label(window, text = "Title")
l1.grid(row=0, column=0)

l2 = Label(window, text = "Author")
l1.grid(row=0, column=2)

l3 = Label(window, text = "Year")
l1.grid(row=1, column=0)

l4 = Label(window, text = "ISBN")
l1.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e1.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e1.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e1.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35, rowspan=6, columnspan=2)
list1.grid(row=2, column=0)

sb1 = Scrolbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscorllcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "View all")
b1.grid(row=2, column=3)

b1 = Button(window, text = "Search entry")
b1.grid(row=2, column=3)

b1 = Button(window, text = "Add entry")
b1.grid(row=3, column=3)

b1 = Button(window, text = "Update")
b1.grid(row=4, column=3)

b1 = Button(window, text = "Delete")
b1.grid(row=5, column=3)

b1 = Button(window, text = "Close")
b1.grid(row=6, column=3)

window.mainloop()

