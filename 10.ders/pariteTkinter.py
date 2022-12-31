from tkinter import *
from tkinter import ttk
from tkinter import messagebox

Parite = TarihBaslangic = TarihBitis = None

root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()
root.geometry("250x250")
ttk.Label(frm, text="Parite").grid(column=0, row=0)
Parite = Entry(frm, width = 10 )
Parite.grid(column = 1, row = 0)
ttk.Label(frm, text="Tarih Başlangıç").grid(column=0, row=1)
TarihBaslangic = Entry(frm, width = 10 )
TarihBaslangic.grid(column = 1, row = 1)
ttk.Label(frm, text="Tarih Bitiş").grid(column=0, row=2)
TarihBitis = Entry(frm, width = 10 )
TarihBitis.grid(column = 1, row = 2)

def control():
    if txt == "a" and "a" == txt2:
        frm = ttk.Frame(root, padding=40)
        frm.grid()
        root.geometry("250x250")
        ttk.Label(frm, text="Kullanıcı Adı").grid(column=0, row=0)
    else:
        messagebox.showwarning("Warning","Warning message for user")
        root.mainloop()
ttk.Button(frm, text="Göster", command=control).grid(column=1, row=4)
root.mainloop()