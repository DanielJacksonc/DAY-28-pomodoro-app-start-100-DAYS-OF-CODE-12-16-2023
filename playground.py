import time
# def count_down():
#     start_button.get()
#
#     for i in range (1,9):
#         if i < 6:
#             print(i)
#             time.sleep(1)

# count = count_down()
def counter(n ):
    while True:
        if n >= 0:
            n -=1
            print(n+1)
            time.sleep(2)
counter(5)





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
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
fg = GREEN
timer_label.grid(column=1,row=0)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

start_button = Button(text="start", highlightthickness=0)
start_button.grid(column=0, row=2)

timer_check = Label(text="🗸", fg=GREEN, bg=YELLOW, font=(60))
timer_check.grid(column=1, row=3)

window.mainloop()