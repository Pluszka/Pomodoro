from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#F0B67F"
RED = "#E23428"
GREEN = "#75BBA7"
BLUE = "#6C809A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
SEC = 1000
reps = 0
just_timer = None
time_left = None
# ---------------------------- TIMER RESET & PAUSE ------------------------------- #


def restart():
    global just_timer
    root.after_cancel(just_timer)
    title_label.config(text='Timer')
    canvas.itemconfig(timer_txt, text='00:00')
    check_marks_label.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time(count_value=False):
    global reps
    reps += 1
    if count_value:
        pass
    elif reps % 8 == 0:
        title_label.config(text='Long Break', fg=RED)
        count_value = LONG_BREAK_MIN
    elif reps % 2 == 1:
        title_label.config(text='Work', fg=GREEN)
        count_value = WORK_MIN
    else:
        title_label.config(text='Short Break', fg=ORANGE)
        count_value = SHORT_BREAK_MIN
    count_down(count_value * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global time_left
    time_left = count - 1
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_txt, text=f'{count_min}:{count_sec}')
    if count > 0:
        global just_timer
        just_timer = root.after(SEC, count_down, count-1)
    else:
        if reps % 2 == 0:
            add_mark()
        start_time()


def add_mark():
    current_txt = check_marks_label.get('text')
    current_txt += CHECK_MARK
    check_marks_label.config(text=current_txt)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Pomodoro')
root.config(padx=40, pady=40, bg=BLUE)

canvas = Canvas(width=300, height=250, highlightthickness=0, bg=BLUE)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(150, 120, image=tomato)
timer_txt = canvas.create_text(150, 140, text="00:00", fill=BLUE, font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=BLUE, anchor='s', font=(FONT_NAME, 35, 'bold'), fg=GREEN)
title_label.grid(row=0, column=1)

check_marks_label = Label(anchor='n', bg=BLUE, font=(FONT_NAME, 12, 'bold'), fg=GREEN)
check_marks_label.grid(row=2, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED, command=start_time)
start_button.grid(row=3, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), bg=GREEN, fg=RED, command=restart)
reset_button.grid(row=3, column=3)

root.mainloop()
