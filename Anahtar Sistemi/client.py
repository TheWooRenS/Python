from customtkinter import *
from CTkListbox import *
from CTkMessagebox import CTkMessagebox
import sqlite3
import time
import uuid

db = sqlite3.Connection("database.sqlite")
cursor = db.cursor()

root = CTk()
root.geometry("1020x850")
root.title("Key")

keytitle = CTkLabel(root, text="")
keytitle.place(x=0, y=130)
keytitle.forget()


def selectiteminyeslist(select):
    keytitle.configure(text=select)
    for i in range(nolist.size()):
        nolist.deactivate(i)

def selectiteminnolist(select):
    keytitle.configure(text=select)
    for i in range(yeslist.size()):
        yeslist.deactivate(i)

text1 = CTkLabel(root, text="Kullanılmış Keyler", text_color="white", width=25, height=25)
text1.place(x=125,y=20)
yeslist = CTkListbox(root,width=350 ,height=350,command=selectiteminyeslist,text_color="red", fg_color="black", hover_color="orange",button_color="white", highlight_color="orange")
yeslist.place(x=0, y=45)
text2 = CTkLabel(root, text="Kullanılmamış Keyler", text_color="white", width=25, height=25)
text2.place(x=125,y=450)
nolist = CTkListbox(root,width=350, height=350, command=selectiteminnolist, text_color="green", fg_color="black", hover_color="orange",button_color="white", highlight_color="orange")
nolist.place(x=0, y=475)

def getValues():
    db = sqlite3.Connection("database.sqlite")
    cursor = db.cursor()  
    cursor.execute("select value, use from keys")
    rows = cursor.fetchall()
    for row in rows:
        if (row[-1] == 'no'):
            nolist.insert("END", row[0])
        else:
            yeslist.insert("END", row[0])
    db.close()
    keytitle.configure(text="")


def usedKey():
    key = keytitle.cget("text")
    if len(key) < 5:
        show_error()
    else:
        db = sqlite3.Connection("database.sqlite")
        cursor = db.cursor()
        cursor.execute("""
                        UPDATE keys SET use = ? WHERE value = ?;
                    """, ("yes", key))
        db.commit()
        yeslist.delete(0,'END')
        nolist.delete(0,'END')
        time.sleep(1)
        getValues()
        db.close()
        keytitle.configure(text="")

def RusedKey():
    db = sqlite3.Connection("database.sqlite")
    key = keytitle.cget("text")
    cursor = db.cursor()
    cursor.execute("""
                    UPDATE keys SET use = ? WHERE value = ?;
                   """, ("no", key))
    db.commit()
    yeslist.delete(0,'END')
    nolist.delete(0,'END')
    time.sleep(1)
    getValues()
    db.close()
    keytitle.configure(text="")

def createKey():
    db = sqlite3.Connection("database.sqlite")
    cursor = db.cursor()
    cursor.execute("""INSERT INTO keys(id, value, use) 
                VALUES (NULL,?,?);""", (str(uuid.uuid4()), "no"))
    db.commit()
    yeslist.delete(0,'END')
    nolist.delete(0,'END')
    time.sleep(0.4)
    getValues()
    db.close()
    keytitle.configure(text="")

def deleteKey():
    db = sqlite3.Connection("database.sqlite")
    key = keytitle.cget("text")
    cursor = db.cursor()
    cursor.execute("""DELETE FROM keys WHERE value=?;""", [key])
    db.commit()
    yeslist.delete(0,'END')
    nolist.delete(0,'END')
    time.sleep(1)
    getValues()
    db.close()
    keytitle.configure(text="")

def show_warning():
    msg = CTkMessagebox(title="Warning Message!", message="Veri Tabanı Silinecek Kabul Ediyor musunuz?",
                  icon="warning", option_1="İptal", option_2="Temizle")
    
    if msg.get()=="Temizle":
        db = sqlite3.Connection("database.sqlite")
        key = keytitle.cget("text")
        cursor = db.cursor()
        cursor.execute("DELETE FROM keys")
        db.commit()
        yeslist.delete(0,'END')
        nolist.delete(0,'END')
        time.sleep(1)
        getValues()
        db.close()
        keytitle.configure(text="")
    else:
        pass


def show_error():
    CTkMessagebox(title="Hata", message="İşlem yapabilmek için lütfen listeden bir KEY seçiniz!", icon="cancel")

clearbtn = CTkButton(root, text="Kullanıldı Olarak İşaretle ", command=usedKey)
clearbtn.place(x=395, y=80)

clearbtn2 = CTkButton(root, text="Kullanılmadı Olarak İşaretle ", command=RusedKey)
clearbtn2.place(x=395, y=120)

createbtn = CTkButton(root, text="Yeni Bir Key Oluştur", command=createKey)
createbtn.place(x=395, y=160)

deletebtn = CTkButton(root, text="Sil", command=deleteKey)
deletebtn.place(x=395, y=200)

deletebtn = CTkButton(root, text="Veri Tabanını Temizle", command=show_warning)
deletebtn.place(x=395, y=240)

getValues()


root.mainloop()