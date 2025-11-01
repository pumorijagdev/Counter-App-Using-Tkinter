import tkinter as tk

screen = tk.Tk()
screen.title("Counter App")
screen.geometry("600x400")
screen.config(bg="#1e1e2e")


title_label = tk.Label(
    text="Counter App",
    font=("Arial", 30, "bold"),
    fg="#00BCD4",
    bg="#1e1e2e"
)
title_label.place(x=220, y=50)

count = tk.IntVar(value=0)

count_var = tk.Label(textvariable=count,font=("Arial",40,"bold"),fg="#f9f9f9",bg="#1e1e2e")
count_var.place(x=300, y=130)

def increase():
    count.set(count.get() + 1)
increase_btn = tk.Button(text="+",width=8,font=("Arial",15,"bold"),  bg="#4CAF50", fg="white",command=increase)
increase_btn.place(x=180, y=250)

def decrease():
    if count.get() >  0:
        count.set(count.get() - 1)
decrease_btn = tk.Button(text="-",width=8,font=("Arial",15,"bold"),bg="#f44336",fg="white",command=decrease)
decrease_btn.place(x=360, y=250)

def reset():
    count.set(0)
reset_btn = tk.Button(text="Reset",width=10,font=("Arial",12,"bold"), bg="#2196F3", fg="white",command=reset)
reset_btn.place(x=270, y=330)


screen.mainloop()