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
        l1.grid(row=0, column=2)

        l3 = Label(self.window, text = "Year")
        l1.grid(row=1, column=0)

        l4 = Label(self.window, text = "ISBN")
        l1.grid(row=1, column=2)

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

        self.list1 = Listbox(self.window, height=6, width=35, rowspan=6, columnspan=2)
        self.list1.grid(row=2, column=0)
        self.list1.bind('<<ListboxSelect>>' get_selected_row)

        sb1 = Scrolbar(self.window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.configure(yscorllcommand = sb1.set)
        sb1.configure(command = self.list1.yview)

        b1 = Button(self.window, text = "View all", command = view_command)
        b1.grid(row=2, column=3)

        b1 = Button(self.window, text = "Search entry", command = search_command)
        b1.grid(row=2, column=3)

        b1 = Button(self.window, text = "Add entry", command = add_command)
        b1.grid(row=3, column=3)
 
        b1 = Button(self.window, text = "Update", command = update_command)
        b1.grid(row=4, column=3)
 
        b1 = Button(self.window, text = "Delete", command = delete_command)
        b1.grid(row=5, column=3)

        b1 = Button(self.window, text = "Close", command = self.window.destroy)
        b1.grid(row=6, column=3) 
                              
    def view_command():
        self.list1.delete(0, END)
        for row in backend.view():
            self.list1.insert(END, row)
        
    def search_command():
        self.list1.delete(0, END)
        for row in backend.search(self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get())):
            self.list1.insert(END, row)
        
    def add_command():
        backend.insert(self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get()))
        self.list1.delete(0, END)
        self.list1.insert(END, self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get()))

    def get_selected_row(event):
        try:
            global selected_id
            selected_id.curselecion()[0]
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.insert(END, selected_tuple[2])
            self.e3.insert(END, selected_tuple[3])
            self.e4.insert(END, selected_tuple[4])
            return selected_tuple
        except:
            pass

    def delete_command():
        backend.delete(selected_id)
    
    def update_command():
        backend.update(selected_id, self.title_text.get(), self.author_text.get(), int(self.year_text.get()), int(self.isbn_text.get())
                   
window = Tk()
Window(window)
window.mainloop()
