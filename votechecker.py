import customtkinter as ctk
app = ctk.CTk()
app.title("Vote Eligibility Checker")
app.geometry("500x400")

def check():
    try:
        a = int(age.get())
        if a>=18:
            label.configure(text = f"Your age is {a}\nYes You are eligible to Vote")
        else:
            label.configure(text = f"Your age is {a}\nNo You aren't eligibe to Vote")
    except ValueError:
        label.configure(text="Enter a Number")
        return
    age.delete(0,"end")

label = ctk.CTkLabel(app, text="Check Your Eligibilty Here")
label.pack(pady = 20)

age = ctk.CTkEntry(app, placeholder_text="Enter Your Age")
age.pack(pady = 10)

button = ctk.CTkButton(app,text="Check",command=check)
button.pack(pady = 10)


app.mainloop()
