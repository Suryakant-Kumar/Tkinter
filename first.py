import customtkinter as ctk

app = ctk.CTk()
app.title("Lesson 1")
app.geometry("500x400")

label = ctk.CTkLabel(app,text="Hello There")
label.pack(pady=20)

def changetext():
    label.configure(text = "You clicked me!!")
    button.configure(text = "Yaay!!")
    button.pack(ipadx = 50)


button = ctk.CTkButton(app,text="Click me !!",command=changetext)


button.pack(pady = 20)
button.pack(ipadx=100)

app.mainloop()
