from io import BytesIO
from tkinter import *
from tkinter import messagebox
import string
import random
from captcha.image import ImageCaptcha
from time import sleep

image = ImageCaptcha(fonts=['DejaVuSanssr.ttf', 'ChelseaMarketsr.ttf'])

random_=''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
data = image.generate(random_)
assert isinstance(data, BytesIO)
image.write(random_,'out.png')

def refresh():
        global random_
        random_=''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        data = image.generate(random_)
        assert isinstance(data, BytesIO)
        image.write(random_,'out.png')
        photo = PhotoImage(file="out.png")
        l1.config(image=photo,height=100,width=200)
        l1.configure(image=photo)
        l1.image = photo


def verify():
    global random_
    x=t1.get("0.0",END)

    if (x.strip()==random_):
        messagebox.showinfo("sucsess", "verified")
        root.destroy()
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()


root=Tk()
photo = PhotoImage(file="out.png")

l1=Label(root,image=photo,height=100,width=200)
t1=Text(root,height=1,width=50)
b1=Button(root,text="submit",command=verify)
b2=Button(root,text="refresh",command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()