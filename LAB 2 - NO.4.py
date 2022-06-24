from tkinter import*
from tkinter import messagebox

count = 3

def login():
    var_pin = entry1.get()
    pin = 12345
    global count


    if var_pin.isdigit():

        var_pin = int(var_pin)

        if var_pin == pin:
            messagebox.showinfo("Successful", "Login Successful")

        else:
            messagebox.showerror("Error", "Incorrect Password" + "\n   Attempts left: " + str(count - 1))
            count -= 1
            print(count)

    else:
        messagebox.showerror("Error", "Incorrect Password" + "\n   Attempts left: " + str(count - 1))
        count -= 1
        print(count)

    if count == 0:
        messagebox.showerror("Error", "   Incorrect Password" + "\n THIS ACTION IS ILLEGAL")
        breakpoint()

root = Tk()
root.title("ATM")
root.geometry("300x200")

global entry1

Label(root, text="Enter your Pin").place(x=40, y=20)


entry1 = Entry(root, bd=5)
entry1.place(x=90, y=55 )

Button(root, text="Login", command=login, height=3, width=13, bd=6). place(x=100, y=120)



root.mainloop()

