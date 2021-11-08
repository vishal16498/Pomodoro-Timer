from tkinter import *

window = Tk()
window.title("Pomodoro Timer for Productivity")
window.config(padx=120, pady=60, bg="#3F3351")

title_label = Label(text="Timer", font=("Comic sans", 40, "bold"), fg="#B1E693", bg="#3F3351")
title_label.grid(column=1, row=0)

WORK_TIME = 25*60
SHORT_BREAK = 5*60
LONG_BREAK = 20*60
reps = 0
timer = None


def count_down(count):
    count_minute = count // 60
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        # add tick mark every 2 reps
        start_timer()
        marks = ""  # empty string, easier to append the text
        for _ in range(reps//2):
            marks += "✔"
        check_mark.config(text=marks)


def start_timer():
    global reps
    reps += 1
# logic for long break and reset the cycle
    if reps % 8 == 0:
        count_down(LONG_BREAK)
        title_label.config(text="Long Break", fg="red")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK)
        title_label.config(text="Break Time", fg="pink")
    else:
        count_down(WORK_TIME)
        title_label.config(text="Work", fg="light green", font=("Comic sans", 40, "bold"))


def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0


canvas = Canvas(width=200, height=224, bg="#3F3351", highlightthickness=0)
image_canvas = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_canvas)
timer_text = canvas.create_text(100, 130, text="00:00", fill="#000000", font=("Comic sans", 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=("Arial", 15, "normal"), command=start_timer)  # button to start the timer
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=("Arial", 15, "normal"), command=reset_timer)   # button to reset the timer to 0
reset_button.grid(column=2, row=3)

check_mark = Label(fg="#6ECB63", bg="#3F3351", font=("Arial", 16, "bold"))
check_mark.grid(column=1, row=4)

#   mainloop is an event
window.mainloop()
