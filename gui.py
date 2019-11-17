from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if part_text.get() != '' or customer_text.get() != '' or retailer_text.get() or price_text.get() != '':
        db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
        parts_list.delete(0, END)
        parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
        clear_text()
        populate_list()
    else:   
        messagebox.showerror('Nödvändiga fält', 'Nu glömde nu något! ')
        return  
   
def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0],part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()

def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

#Create window
app = Tk()

#Part
part_text = StringVar()
part_label = Label(app, text='Pryl Namn', font=('bold', 14), pady=20, padx=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable = part_text, border=0, font=(14))
part_entry.grid(row=0, column= 1)

#Customer
customer_text = StringVar()
customer_label = Label(app, text='Namn', font=('bold', 14), padx=20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable = customer_text, border=0, font=(14))
customer_entry.grid(row=0, column= 3)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Försäljare', font=('bold', 14), padx=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable = retailer_text, border=0, font=(14))
retailer_entry.grid(row=1, column= 1)

#Price
price_text = StringVar()
price_label = Label(app, text='Pris', font=('bold', 14), padx=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable = price_text, border=0, font=(14))
price_entry.grid(row=1, column= 3)

#Parts lists
parts_list = Listbox(app, height=10, width=75, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, padx=20 )

#Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

#Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3, rowspan=6,sticky=N+S)

#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#Buttons
add_btn = Button(app, text='Lägg till', width=12, command=add_item, background = '#6f9e6f', foreground='white', border=0, activebackground='#c0eac0', font=('bold'))
add_btn.grid(row=2, column=0,pady=20)

remove_btn = Button(app, text='Ta bort', width=12, command=remove_item, background='#c22626', foreground='white', border=0, font=('bold'), activebackground='#f5a6a6')
remove_btn.grid(row=2, column=3)

update_btn = Button(app, text='Uppdatera', width=12, command=update_item, background='#FFC300', foreground='white', border=0, font=('bold'), activebackground='#c0eac0')
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Rensa input', width=12, command=clear_text, background='#d0dd00', foreground='white', border=0, font=('bold'),activebackground='#c0eac0')
clear_btn.grid(row=2, column=1)

app.title('List Manager')
app.configure(background ='#eaf1ea')
app.geometry('700x400')

#Populate data
populate_list()

#start program
app.mainloop()
