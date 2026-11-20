import customtkinter as ctk

app = ctk.CTk()
app.title("Square Calculator")
app.geometry("300x200")
def square():
    try:
        n = int(entry.get())
        label.configure(text = f"The Square of {n} is {n*n}")
    except ValueError:
        label.configure(text = "Enter a valid integer")
        return
    entry.delete(0, "end")
    
label = ctk.CTkLabel(app, text="Calculate the Square Here")
label.pack(pady = 20)

entry = ctk.CTkEntry(app,placeholder_text="Enter the Number")
entry.pack(pady=10)

button = ctk.CTkButton(app,text="Calculate",command=square)
button.pack(pady=10)

app.mainloop()