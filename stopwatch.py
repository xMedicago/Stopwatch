import tkinter as tk
from datetime import datetime

start_time = 0
after_id = ""


def stopwatch():
    global start_time, after_id
    after_id = root.after(1000, stopwatch)
    f_start_time = datetime.fromtimestamp(start_time).strftime("%M:%S")
    label_1.configure(text=str(f_start_time))
    start_time += 1


def start_button():
    first_button.grid_forget()
    second_button.grid(row=1, columnspan=2, sticky="ew")
    stopwatch()


def stop_button():
    second_button.grid_forget()
    third_button.grid(row=1, column=0, sticky="ew")
    fourth_button.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)


def continue_button():
    third_button.grid_forget()
    fourth_button.grid_forget()
    second_button.grid(row=1, columnspan=2, sticky="ew")
    stopwatch()


def reset_button():
    global start_time
    start_time = 0
    label_1.configure(text="00:00")
    third_button.grid_forget()
    fourth_button.grid_forget()
    first_button.grid(row=1, columnspan=2, sticky="ew")


root = tk.Tk()
root.resizable(False, False)
root.title("Секундомер")

label_1 = tk.Label(root, width=5, font=("Ubuntu", 100), text="00:00")
label_1.grid(row=0, columnspan=2)

first_button = tk.Button(root, font=("Ubuntu", 30), text="Start", command=start_button, background="#cd853f")
second_button = tk.Button(root, font=("Ubuntu", 30), text="Stop", command=stop_button, background="red")
third_button = tk.Button(root, font=("Ubuntu", 30), width=5, text="Continue", command=continue_button, background="yellow")
fourth_button = tk.Button(root, font=("Ubuntu", 30), width=5, text="Reset", command=reset_button, background="#AD8AAA")

first_button.grid(row=1, columnspan=2, sticky="ew")

if __name__ == '__main__':
    root.mainloop()