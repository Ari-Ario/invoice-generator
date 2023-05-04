from tkinter import *

class Invoice():
    def __init__(self, master):
        self.master= master

        self._all_Widgets()

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

        self.main_win.pack(fill=BOTH, padx=10, pady=10)
        self.label_first_name.grid(row=0, column=0)
        self.label_second_name.grid(row=0, column=1)
        self.entry_first_name.grid(row=1, column=0)
        self.entry_second_name.grid(row=1, column=1)
        self.label_phone_num.grid(row=0, column=2)
        self.entry_phone_num.grid(row=1, column=2)
        #grids of second row
        self.label_quantity.grid(row=2, column=0)
        self.spinbox_quantity.grid(row=3, column=0)
        self.label_description.grid(row=2, column=1)
        self.entry_description.grid(row=3, column=1)
        self.label_unitprice.grid(row=2, column=2)
        self.spinbox_unitprice.grid(row=3, column=2)

if __name__ == "__main__":
    app = Tk()
    app.title("INVOICE GENERATOR")
    Invoice(app)
    app.mainloop()