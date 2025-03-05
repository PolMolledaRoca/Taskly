import tkinter as tk
from tkinter import messagebox, ttk
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def remove_task():
    try:
        selected_task = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task)
        del tasks[selected_task]
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")

def clear_tasks():
    global tasks
    tasks = []
    save_tasks(tasks)
    listbox_tasks.delete(0, tk.END)

# Load existing tasks
tasks = load_tasks()

# GUI Setup
window = tk.Tk()
window.title("To-Do List")
window.geometry("450x500")
window.configure(bg="#2c3e50")

style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", background="#2c3e50", foreground="white", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

frame = tk.Frame(window, bg="#2c3e50")
frame.pack(pady=10)

title_label = ttk.Label(frame, text="📝 To-Do List", font=("Arial", 16, "bold"))
title_label.pack()

entry_task = ttk.Entry(frame, width=30)
entry_task.pack(pady=10)

button_frame = tk.Frame(frame, bg="#2c3e50")
button_frame.pack()

add_button = ttk.Button(button_frame, text="Add Task", command=add_task, width=12)
add_button.grid(row=0, column=0, padx=5)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task, width=12)
remove_button.grid(row=0, column=1, padx=5)

clear_button = ttk.Button(button_frame, text="Clear All", command=clear_tasks, width=12)
clear_button.grid(row=0, column=2, padx=5)

listbox_frame = tk.Frame(window, bg="#2c3e50")
listbox_frame.pack(pady=10)

listbox_tasks = tk.Listbox(listbox_frame, width=50, height=15, font=("Arial", 12), bg="#ecf0f1")
listbox_tasks.pack()

for task in tasks:
    listbox_tasks.insert(tk.END, task)

window.mainloop()
