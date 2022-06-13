import tkinter as tk
from datetime import datetime


class Stopwatch:
    start_time = 0
    after_id = ""

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Секундомер")
        self.photo = tk.PhotoImage(file="stopwatch_46861.png")
        self.root.iconphoto(False, self.photo)

        self.label_1 = tk.Label(self.root, width=5, font=("Ubuntu", 100), text="00:00")
        self.label_1.grid(row=0, columnspan=2)

        self.first_button = tk.Button(self.root, font=("Ubuntu", 30), text="Start", command=self.start_button,
                                      background="#cd853f",
                                      relief=tk.RAISED, bd=10)
        self.second_button = tk.Button(self.root, font=("Ubuntu", 30), text="Stop", command=self.stop_button,
                                       background="red",
                                       relief=tk.RAISED, bd=10)
        self.third_button = tk.Button(self.root, font=("Ubuntu", 30), width=5, text="Continue",
                                      command=self.continue_button,
                                      background="yellow", relief=tk.RAISED, bd=10)
        self.fourth_button = tk.Button(self.root, font=("Ubuntu", 30), width=5, text="Reset", command=self.reset_button,
                                       background="#AD8AAA",
                                       relief=tk.RAISED, bd=10)

        self.first_button.grid(row=1, columnspan=2, sticky="ew")

    def stopwatch(self):
        self.after_id = self.root.after(1000, self.stopwatch)
        hours, minutes, seconds = self.start_time // 3600, (self.start_time % 3600) // 60, self.start_time % 60
        f_start_time = datetime.strptime(f"{hours}:{minutes}:{seconds}", "%H:%M:%S").strftime("%H:%M:%S")
        self.label_1.configure(text=str(f_start_time))
        self.start_time += 1

    def start_button(self):
        self.first_button.grid_forget()
        self.second_button.grid(row=1, columnspan=2, sticky="ew")
        self.stopwatch()

    def stop_button(self):
        self.second_button.grid_forget()
        self.third_button.grid(row=1, column=0, sticky="ew")
        self.fourth_button.grid(row=1, column=1, sticky="ew")
        self.root.after_cancel(self.after_id)

    def continue_button(self):
        self.third_button.grid_forget()
        self.fourth_button.grid_forget()
        self.second_button.grid(row=1, columnspan=2, sticky="ew")
        self.stopwatch()

    def reset_button(self):
        self.start_time = 0
        self.label_1.configure(text="00:00")
        self.third_button.grid_forget()
        self.fourth_button.grid_forget()
        self.first_button.grid(row=1, columnspan=2, sticky="ew")


if __name__ == '__main__':
    Stopwatch().root.mainloop()
