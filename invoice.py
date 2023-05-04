from tkinter import *

class Invoice():
    def __init__(self, master):
        self.master= master


if __name__ == "__main__":
    app = Tk()
    app.title("INVOICE GENERATOR")
    Invoice(app)
    app.mainloop()