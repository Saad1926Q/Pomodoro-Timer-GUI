from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#ebe3c3"
BLUE="#407f77"
ORANGE="#fb641d"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps+=1

    if reps%8==0:
        count=LONG_BREAK_MIN
        timer_label.config(text="Break")
    elif reps%2==0:
        count=SHORT_BREAK_MIN
        timer_label.config(text="Break")
    else:
        count=WORK_MIN
        timer_label.config(text="Work")

    count_down(count*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min=int(count/60)
    count_seconds=count%60
    formatted_min=str(count_min).zfill(2)
    formatted_sec=str(count_seconds).zfill(2)
    canvas.itemconfig(timer_text,text=f"{formatted_min}:{formatted_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=int(reps/2)
        for i in range(work_sessions):
            mark+="✔"
        check_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Timer GUI")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=224,height=224,bg=YELLOW,highlightthickness=0)
pomodoro_img=PhotoImage(file="pomodoro2.png")
canvas.create_image(112,112,image=pomodoro_img)
timer_text=canvas.create_text(112,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

timer_label=Label(text="Timer",bg=YELLOW,font=(FONT_NAME,40,"normal"),fg=BLUE)
timer_label.grid(column=1,row=0)



start_button=Button(text="start",borderwidth=0,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)


reset_button=Button(text="reset",borderwidth=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_label=Label(bg=YELLOW,font=(FONT_NAME,20,"normal"),fg=BLUE)
check_label.grid(column=1,row=3)




window.mainloop()