from tkinter import *
import backend

global selected_tuple


def clear_and_view():
    listOfBooks.delete(0, END)
    for row in backend.view():
        listOfBooks.insert(END, row)


window = Tk()

titleLabel = Label(window, text="Title")
titleLabel.grid(row=0, column=0)

title_text = StringVar()
titleEntry = Entry(window, textvariable=title_text)
titleEntry.grid(row=0, column=1)

authorLabel = Label(window, text="Author")
authorLabel.grid(row=0, column=2)

author_text = StringVar()
authorEntry = Entry(window, textvariable=author_text)
authorEntry.grid(row=0, column=3)

yearLabel = Label(window, text="Year")
yearLabel.grid(row=1, column=0)

year_text = StringVar()
yearEntry = Entry(window, textvariable=year_text)
yearEntry.grid(row=1, column=1)

ISBNLabel = Label(window, text="ISBN")
ISBNLabel.grid(row=1, column=2)

isbn_text = StringVar()
ISBNEntry = Entry(window, textvariable=isbn_text)
ISBNEntry.grid(row=1, column=3)

listOfBooks = Listbox(window, height=6, width=35)
listOfBooks.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)


def get_selected_row(event):
    global selected_tuple
    index = listOfBooks.curselection()
    if len(index) > 0:
        selected_tuple = listOfBooks.get(index[0])
        titleEntry.delete(0, END)
        titleEntry.insert(0, selected_tuple[1])
        authorEntry.delete(0, END)
        authorEntry.insert(0, selected_tuple[2])
        yearEntry.delete(0, END)
        yearEntry.insert(0, selected_tuple[3])
        ISBNEntry.delete(0, END)
        ISBNEntry.insert(0, selected_tuple[4])


listOfBooks.bind('<<ListboxSelect>>', get_selected_row)


def view_command():
    clear_and_view()


viewButton = Button(window, text="View All", width=12, command=view_command)
viewButton.grid(row=2, column=3)


def search_command():
    listOfBooks.delete(0, END)
    print(title_text.get())
    for row in backend.search(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get()):
        listOfBooks.insert(END, row)


searchButton = Button(window, text="Search Entry", width=12, command=search_command)
searchButton.grid(row=3, column=3)


def add_command():
    backend.insert(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get())
    clear_and_view()


addButton = Button(window, text="Add Entry", width=12, command=add_command)
addButton.grid(row=4, column=3)


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    clear_and_view()
        

updateButton = Button(window, text="Update Entry", width=12, command=update_command)
updateButton.grid(row=5, column=3)


def delete_command():
    backend.delete(selected_tuple[0])
    clear_and_view()


deleteButton = Button(window, text="Delete Entry", width=12, command=delete_command)
deleteButton.grid(row=6, column=3)

closeButton = Button(window, text="Close", width=12)
closeButton.grid(row=7, column=3)

listOfBooks.configure(yscrollcomman=scroll.set)
scroll.configure(command=listOfBooks.yview)


window.mainloop()

