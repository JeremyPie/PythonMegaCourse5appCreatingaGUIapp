from tkinter import *
import backend

window = Tk()

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
        
def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), int(year_text.get()), int(isbn.get())):
        list1.insert(END, row)
        
def add_command():
    backend.insert(title_text.get(), author_text.get(), int(year_text.get()), int(isbn.get()))
    list1.delete(0, END)
    list1.insert(END, title_text.get(), author_text.get(), int(year_text.get()), int(isbn.get()))

    
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

b1 = Button(window, text = "View all", command = view_command)
b1.grid(row=2, column=3)

b1 = Button(window, text = "Search entry", command = search_command)
b1.grid(row=2, column=3)

b1 = Button(window, text = "Add entry", command = add_command)
b1.grid(row=3, column=3)

b1 = Button(window, text = "Update")
b1.grid(row=4, column=3)

b1 = Button(window, text = "Delete")
b1.grid(row=5, column=3)

b1 = Button(window, text = "Close")
b1.grid(row=6, column=3)

window.mainloop()
