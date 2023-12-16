
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ''

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    timer_check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 ==0:
        counter(long_break_sec)
        timer_label = Label(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
        timer_label.grid(column=1, row=0)
    elif reps % 2 == 0:
        counter(short_break_sec)
        timer_label = Label(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
        timer_label.grid(column=1, row=0)
    else:
        counter(work_sec)
        timer_label = Label(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
        timer_label.grid(column=1, row=0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter (count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = (f"0{count_seconds}")
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, counter, count - 1)

    else:
        start_count()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "🗸"
        timer_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
import math


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"), )
timer_label.grid(column=1, row=0)

reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

start_button = Button(text="start", highlightthickness=0, command=start_count)
start_button.grid(column=0, row=2)

timer_check = Label(fg=GREEN, bg=YELLOW, font=(60))
timer_check.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_label.grid(column=1, row=0)

window.mainloop()
