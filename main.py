import math
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
#CHECK_MARK = "✔"
reps = 0
timer=NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer",fg=GREEN)
    check_marks.config(text='')
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text="{0:02d}:{1:02d}".format(count_min, count_sec))
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks=''
        work_session=math.floor(reps/2)
        for _ in range(work_session):
           marks+="✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 114, image=tomato_img)
timer_text = canvas.create_text(105, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label
title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)
check_marks = Label(text='', font=(FONT_NAME, 20, "bold"),fg=GREEN)
check_marks.grid(column=1, row=2)

# Buttons
start_but = Button(text="Start", width=8, command=start_timer)
start_but.grid(column=0, row=2)
reset_but = Button(text="Reset", width=8,command=reset_timer)
reset_but.grid(column=2, row=2)

window.mainloop()
