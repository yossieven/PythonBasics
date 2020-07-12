from tkinter import *
import backend

window = Tk()

titleLabel = Label(window, text="Title")
titleLabel.grid(row=0, column=0)

authorLabel = Label(window, text="Author")
authorLabel.grid(row=0, column=2)

yearLabel = Label(window, text="Year")
yearLabel.grid(row=1, column=0)

ISBNLabel = Label(window, text="ISBN")
ISBNLabel.grid(row=1, column=2)

isbn_text = StringVar()
ISBNEntry = Entry(window, textvariable=isbn_text)
ISBNEntry.grid(row=0, column=1)

author_text = StringVar()
authorEntry = Entry(window, textvariable=author_text)
authorEntry.grid(row=0, column=3)

year_text = StringVar()
yearEntry = Entry(window, textvariable=year_text)
yearEntry.grid(row=1, column=1)

listOfBooks = Listbox(window, height=6, width=35)
listOfBooks.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

viewButton=Button(window, text="View All", width=12)
viewButton.grid(row=2, column=3)

searchButton=Button(window, text="Search Entry", width=12)
searchButton.grid(row=3, column=3)

addButton=Button(window, text="Add Entry", width=12)
addButton.grid(row=4, column=3)

updateButton=Button(window, text="Update Entry", width=12)
updateButton.grid(row=5, column=3)

deleteButton=Button(window, text="Delete Entry", width=12)
deleteButton.grid(row=6, column=3)

closeButton=Button(window, text="Close", width=12)
closeButton.grid(row=7, column=3)


listOfBooks.configure(yscrollcomman=scroll.set)
scroll.configure(command=listOfBooks.yview)

isbn_text = StringVar()
ISBNEntry = Entry(window, textvariable=isbn_text)
ISBNEntry.grid(row=1, column=3)



window.mainloop()
