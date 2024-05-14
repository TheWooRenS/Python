import customtkinter
import weather
import texts

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk() 
windowWidth = app.winfo_screenwidth()
windowHeight = app.winfo_screenheight()
x = (windowWidth - 400) // 2
y = (windowHeight - 600) // 2
app.geometry(f"{400}x{600}+{x}+{y}")
app.title("Hava Durumu Uygulaması")

combobox_var = customtkinter.StringVar(value=texts.comboboxtext)  

def combobox_callback(choice):
    statusLabel.configure(text=weather.Weather.get_weather(choice))
        
combobox = customtkinter.CTkComboBox(master=app, font=("Batang", 26, "normal") ,values=texts.citys, command=combobox_callback, variable=combobox_var, justify="center")
combobox.pack(fill=customtkinter.X, pady=25)
combobox.bind("<KeyPress>", lambda e: "break")


statusLabel = customtkinter.CTkLabel(master=app, text=texts.nostatustext, font=("Batang", 32, "normal") )
statusLabel.pack(pady=50) 

app.mainloop()
