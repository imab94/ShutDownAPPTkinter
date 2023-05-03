import tkinter as tk
import subprocess
import time
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("ShutDown App")

        self.label = tk.Label(master, text="Welcome to my App")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10,sticky='ne')

        self.restart_var = tk.BooleanVar()
        self.restart_checkbox = tk.Checkbutton(master, text="Restart", variable=self.restart_var, bg="#f0f0f0",
                                               fg="#444444")
        self.restart_checkbox.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.shutdown_var = tk.BooleanVar()
        self.shutdown_checkbox = tk.Checkbutton(master, text="Shutdown", variable=self.shutdown_var, bg="#f0f0f0",
                                                fg="#444444")
        self.shutdown_checkbox.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        self.proceed_button = tk.Button(master, text="Proceed", command=self.proceed_action, bg="#4caf50", fg="white",
                                        activebackground="#388e3c")
        self.proceed_button.grid(row=2, column=0, padx=10, pady=10)

        self.cancel_button = tk.Button(master, text="Cancel", command=master.quit, bg="#f44336", fg="white",
                                       activebackground="#c62828")
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10)


    def proceed_action(self):
        if self.restart_var.get():
            subprocess.call(["shutdown", "-r", "-t", "0"])
        elif self.shutdown_var.get():
            message = "Your computer is going to shutdown within 10 seconds, Hang on"
            messagebox.showwarning("Shutdown", message)
            time.sleep(10)
            subprocess.call(["shutdown", "-s", "-t", "0"])
        else:
            messagebox.showwarning("No selection", "Please select an option to proceed.")


root = tk.Tk()
root.resizable(0,0)
root.geometry("250x130")
app = App(root)
root.mainloop()
