from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("tkinter")
app.geometry("320x420")
app.config(bg="red")
app.resizable(width=False , height=False)

def savedata():
    with open("config.txt", "w") as dosya:
        dosya.write(textbox.get())
        messagebox.showinfo("Bilgi", "Veriler başarıyla kaydedildi!")
        statuslabel.configure(text=textbox.get())

def getdata():
    try:
        with open("config.txt", "r") as dosya:
            return dosya.read()
    except:
        return "veri kaydedilmedi"
textbox = Entry(font="Arial 18 normal", border=0)
textbox.pack(pady=20)

savebutton = Button(text="Verileri Kaydet", font="Arial 18 normal", border=0, command=savedata)
savebutton.pack(pady=20)

statuslabel = Label(text=getdata(), font="Arial 20 italic", bg="red", fg="white")
statuslabel.pack()

app.mainloop()