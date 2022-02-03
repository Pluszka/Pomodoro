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
SEC = 1000
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    canvas.itemconfig(timer_txt, text=count)
    if count > 0:
        root.after(SEC, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=300, height=250, highlightthickness=0, bg=YELLOW)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(150, 120, image=tomato)
timer_txt = canvas.create_text(150, 120, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

count_down(5)

title_label = Label(text="Timer", bg=YELLOW,  anchor='s', font=(FONT_NAME, 35, 'bold'), fg=GREEN)
title_label.grid(row=0, column=1)

check_marks_label = Label(anchor='n', text=CHECK_MARK, bg=YELLOW, font=(FONT_NAME, 12, 'bold'), fg=GREEN)
check_marks_label.grid(row=2, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED)
start_button.grid(row=3, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED)
reset_button.grid(row=3, column=2)

root.mainloop()
