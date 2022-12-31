from tkinter import *
from tkinter import ttk
from tkinter import messagebox

kullanici = "a"
sifre = "a"

root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()
root.geometry("250x250")
ttk.Label(frm, text="Kullanıcı Adı").grid(column=0, row=0)
txt = Entry(frm, width = 10 )
txt.grid(column = 0, row = 1)
ttk.Label(frm, text="Şifre").grid(column=0, row=2)
txt2 = Entry(frm, width = 10 )
txt2.grid(column = 0, row = 3)


def control():
    if txt == "a" and "a" == txt2:
        frm = ttk.Frame(root, padding=40)
        frm.grid()
        root.geometry("250x250")
        ttk.Label(frm, text="Kullanıcı Adı").grid(column=0, row=0)
    else:
        messagebox.showwarning("Warning","Warning message for user")
        root.mainloop()
ttk.Button(frm, text="Giriş", command=control).grid(column=1, row=0)
root.mainloop()