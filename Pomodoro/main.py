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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        text.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        text.config(text="Work", fg=GREEN)
        check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=24)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        total_work_section = math.floor(reps / 2)
        for _ in range(total_work_section):
            marks += "✔"
        check_marks.config(text=marks)
    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=222, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)

timer_text = canvas.create_text(115, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)

text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
text.config(padx=12, pady=12)
text.grid(row=0, column=1)

start_btn = Button(text="Start", command=start_timer, font=FONT_NAME, bg="white", highlightthickness=0)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset_timer, font=FONT_NAME, bg="white", highlightthickness=0)
reset_btn.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=24)
check_marks.grid(row=3, column=1)

window.mainloop()
