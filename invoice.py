from tkinter import *
from tkinter import ttk

class Invoice():
    def __init__(self, master):
        self.master= master

        self._all_Widgets()

    #
    def add_to_tree(self):
        quan= int(self.spinbox_quantity.get())
        desc= self.entry_description.get()
        price= float(self.spinbox_unitprice.get())
        total = quan * price
        lst= [quan, desc, price, total]
        self.tree.insert("", 0, values=lst)

    #
    def generation(self):
        pass

    #
    def new_invoice(self):
        pass


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
        self.button_genrate= Button(self.main_win, text="Generate Inoice", command=self.generation)
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