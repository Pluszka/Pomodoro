from tkinter import *
import math
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
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_time():
    global reps
    reps += 1
    if reps % 8 ==0:
        count_value = LONG_BREAK_MIN
    elif reps % 2 == 1:
        count_value = WORK_MIN
    else:
        count_value = SHORT_BREAK_MIN
    count_down(count_value )
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_txt, text=f'{count_min}:{count_sec}')
    if count > 0:
        root.after(SEC, count_down, count-1)
    else:
        start_time()


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=300, height=250, highlightthickness=0, bg=YELLOW)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(150, 120, image=tomato)
timer_txt = canvas.create_text(150, 140, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=YELLOW,  anchor='s', font=(FONT_NAME, 35, 'bold'), fg=GREEN)
title_label.grid(row=0, column=1)

check_marks_label = Label(anchor='n', text=CHECK_MARK, bg=YELLOW, font=(FONT_NAME, 12, 'bold'), fg=GREEN)
check_marks_label.grid(row=2, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED, command=start_time)
start_button.grid(row=3, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED)
reset_button.grid(row=3, column=2)

root.mainloop()
