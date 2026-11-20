import customtkinter as ctk
app  = ctk.CTk()
app.title("Taking Input")
app.geometry("500x400")


def greet():
    name = entry.get().strip()
    try:
        ag = int(age.get())
    except ValueError:
        label.configure(text="Invalid Age")
        return
        
    if name == "":
        label.configure(text="Hello <Invalid-name>!!")
    else:
        label.configure(text=f"Hello {name} Your age is {ag}!!")
    entry.delete(0, "end")
    age.delete(0, "end")
label = ctk.CTkLabel(app,text="Hello <Name> !!")
label.pack(pady=20)

entry = ctk.CTkEntry(app,placeholder_text="Enter your name",width=300)
entry.pack(pady=10)

age = ctk.CTkEntry(app,placeholder_text = "Enter you age",width=150)
age.pack(pady=10)

button = ctk.CTkButton(app,text="Register Name",command=greet)
button.pack(pady=10)



app.mainloop()