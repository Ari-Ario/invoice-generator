from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import os

class Invoice():
    def __init__(self, master):
        self.master= master
        self.invoice_list= []
        self._all_Widgets()

    #Method to add the fouth column into the tree
    def add_to_tree(self):
        quan= int(self.spinbox_quantity.get())
        desc= self.entry_description.get()
        price= float(self.spinbox_unitprice.get())
        total = quan * price
        lst= [quan, desc, price, total]
        if price != 0:
            self.tree.insert("", 0, values=lst)
            self.invoice_list.append(lst)
        else:
            messagebox.showerror("Zero Insertion", "Unite Price must not be Zero!")
        self.clear_items()

    #Method to generate the invoice as pdf and also as word 
    def invoice_generation(self):
        name = self.entry_first_name.get() + " " + self.entry_second_name.get()
        phone= self.entry_phone_num.get()
        path = f"invoice-{name}{datetime.datetime.now()}.docx" # there must exist a template
        # A template in word-document (.docx) is needed and all items must be rendered
        #but here we add them without template and tables in it
        with open(path, mode="w", encoding="utf-8") as file:
            file.write(str(name)+"\n")
            file.write(str(phone)+"\n")
            file.write(str(self.invoice_list)+"\n")
            subtotal_price= sum(price[3] for price in self.invoice_list)
            salestax= 0.09 #you can change it according tthe location you live in
            total_price = subtotal_price *(1 - salestax)
            file.write("Total: " + str(round(total_price, 2)))
        

    #Method to clear all fields including tree and ready for new entries
    def new_invoice(self):
        self.clear_items()
        self.entry_first_name.delete(0, END)
        self.entry_second_name.delete(0, END)
        self.entry_phone_num.delete(0, END)
        self.tree.delete(*self.tree.get_children())
        self.invoice_list = []

    #Method to clear the forth column: here column 3
    def clear_items(self):
        self.spinbox_quantity.delete(0, END)
        self.spinbox_quantity.insert(0, "1")
        self.entry_description.delete(0, END)
        self.spinbox_unitprice.delete(0, END)
        self.spinbox_unitprice.insert(0, "0.0")


    def _all_Widgets(self):
        self.main_win= LabelFrame(self.master, text="Invoice Information")
        #labels and entries of first row
        self.label_first_name= Label(self.main_win, text="First name", padx=5, pady=5)
        self.entry_first_name= Entry(self.main_win)
        self.label_second_name= Label(self.main_win, text="Second name", padx=5, pady=5)
        self.entry_second_name= Entry(self.main_win)
        self.label_phone_num= Label(self.main_win, text="phone Number")
        self.entry_phone_num= Entry(self.main_win)
        #labels and etries of second row
        self.label_quantity= Label(self.main_win, text="quantity")
        self.spinbox_quantity= Spinbox(self.main_win, from_=1, to= 1000)
        self.label_description= Label(self.main_win, text="Description")
        self.entry_description= Entry(self.main_win)
        self.label_unitprice= Label(self.main_win, text="Unite Price")
        self.spinbox_unitprice= Spinbox(self.main_win, from_=0.0, to=1000, increment=0.5)
        #add_button and treeview
        self.button_add=Button(self.main_win, text="Add Items", command=self.add_to_tree)
        columns= ["quantity", "description", "price", "total"]
        self.tree= ttk.Treeview(self.main_win, columns=columns, show="headings")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("description", text="Description")
        self.tree.heading("price", text="Price")
        self.tree.heading("total", text="Total")
        self.button_genrate= Button(self.main_win, text="Generate Inoice", command=self.invoice_generation)
        self.button_new= Button(self.main_win, text="New Invoice", command=self.new_invoice)

        #grids of rows 1, 2
        self.main_win.pack(fill=BOTH, padx=10, pady=10)
        self.label_first_name.grid(row=0, column=0, padx=5)
        self.label_second_name.grid(row=0, column=1, padx=5)
        self.entry_first_name.grid(row=1, column=0, padx=5, pady=10)
        self.entry_second_name.grid(row=1, column=1, padx=5, pady=10)
        self.label_phone_num.grid(row=0, column=2, padx=5)
        self.entry_phone_num.grid(row=1, column=2, padx=5, pady=10)
        #grids of rows 3, 4
        self.label_quantity.grid(row=2, column=0, padx=5, pady=10)
        self.spinbox_quantity.grid(row=3, column=0, padx=5)
        self.label_description.grid(row=2, column=1, padx=5, pady=10)
        self.entry_description.grid(row=3, column=1, padx=5)
        self.label_unitprice.grid(row=2, column=2, padx=5, pady=10)
        self.spinbox_unitprice.grid(row=3, column=2, padx=5)
        #grids of add-button and treeview
        self.button_add.grid(row=4, column=2, padx=5, pady=10, sticky=E)
        self.tree.grid(row=5, column=0, columnspan=3, padx=5, pady=10)
        self.button_genrate.grid(row=6, column=0, columnspan=3, sticky=EW, padx= 5, pady= 5)
        self.button_new.grid(row=7, column=0, columnspan=3, sticky=EW, padx=5)

if __name__ == "__main__":
    app = Tk()
    app.title("INVOICE GENERATOR")
    Invoice(app)
    app.mainloop()