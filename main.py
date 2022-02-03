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
CHECK_MARK = "✔"
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.config(padx=20, pady=20, bg=YELLOW)

canvas = Canvas(width=300, height=250, highlightthickness=0, bg=YELLOW)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(150, 120, image=tomato)
canvas.create_text(150, 120, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=YELLOW,  anchor='s', font=(FONT_NAME, 35, 'bold'), fg=GREEN)
title_label.grid(row=0, column=1)

check_marks_label = Label(bg=YELLOW)
check_marks_label.grid(row=3, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED)
reset_button.grid(row=2, column=2)

root.mainloop()
