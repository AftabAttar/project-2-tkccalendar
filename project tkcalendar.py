import tkinter as tk
from tkcalendar import Calendar

def get_date():
    selected_date = cal.get_date()
    selected_date_label.config(text="Selected Date: " + selected_date)

root = tk.Tk()
root.title("Calendar Date Picker")

calendar = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
calendar.pack(padx=10, pady=10)

select_date_btn = tk.Button(root, text="Select Date", command=get_date)
select_date_btn.pack(pady=5)

selected_date_label = tk.Label(root, text="Selected Date: None")
selected_date_label.pack(pady=5)

root.mainloop()