from tkinter import *
from backend import Database

database = Database("book.db")

class Window():
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Bookstore")

        l1 = Label(self.window, text = "Title")
        l1.grid(row=0, column=0)

        l2 = Label(self.window, text = "Author")
        l2.grid(row=0, column=2)

        l3 = Label(self.window, text = "Year")
        l3.grid(row=1, column=0)

        l4 = Label(self.window, text = "ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(self.window, textvariable = self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(self.window, textvariable = self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(self.window, textvariable = self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.e4 = Entry(self.window, textvariable = self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(self.window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        sb1 = Scrollbar(self.window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command = self.list1.yview)

        b1 = Button(self.window, text = "View all", command = self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(self.window, text = "Search entry", command = self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(self.window, text = "Add entry", command = self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(self.window, text = "Update", command = self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(self.window, text = "Delete", command = self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(self.window, text = "Close", command = self.window.destroy)
        b6.grid(row=7, column=3)


    def get_selected_row(self, event):
        print(f"{self.list1.curselection()[0]}")
        print(f"{self.list1.get(self.list1.curselection()[0])[0]}")
        try:
            self.selected_id = self.list1.curselection()[0]
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e1.insert(END, self.list1.get(self.selected_id)[1])
            self.e2.insert(END, self.list1.get(self.selected_id)[2])
            self.e3.insert(END, self.list1.get(self.selected_id)[3])
            self.e4.insert(END, self.list1.get(self.selected_id)[4])
            return self.selected_id
        except:
            print("skipped")

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get())):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get()))
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get())))

    def delete_command(self):
        database.delete(self.selected_id + 1)

    def update_command(self):
        database.update(self.selected_id + 1, self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get()))

window = Tk()
Window(window)
window.mainloop()
