from tkinter import *

class Invoice():
    def __init__(self, master):
        self.master= master

        self._all_Widgets()

    def _all_Widgets(self):
        self.main_win= LabelFrame(self.master, text="Fill the Invoice")
        self.label_first_name= Label(self.main_win, text="First name", padx=5, pady=5)
        self.entry_first_name= Entry(self.main_win, text="First name")
        self.label_second_name= Label(self.main_win, text="Second name", padx=5, pady=5)
        self.entry_second_name= Entry(self.main_win, text="First name")

        self.main_win.pack(fill=BOTH, padx=10, pady=10)
        self.label_first_name.grid(row=0, column=0)
        self.label_second_name.grid(row=0, column=1)
        self.entry_first_name.grid(row=1, column=0)
        self.entry_second_name.grid(row=1, column=1)

if __name__ == "__main__":
    app = Tk()
    app.title("INVOICE GENERATOR")
    Invoice(app)
    app.mainloop()