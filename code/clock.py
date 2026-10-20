import tkinter as tk
from datetime import datetime


def update_time():
    time_label.config(text=datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update_time)


root = tk.Tk()
root.title("대충 지은 이름 어쩌구저쩌구")
root.geometry("280x120")
root.resizable(False, False)

time_label = tk.Label(root, font=("맑은 고딕", 32))
time_label.pack(expand=True)

update_time()
root.mainloop()