from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.config(padx=20, pady=20)

canvas = Canvas(width=300, height=250)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(150, 120, image=tomato)

canvas.pack()

root.mainloop()
