import tkinter as tk

class passwrodgenerater:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("420x520")
        self.root.config(bg="#0b032d")

        label=tk.Label(self.root, text="Password Generator", 
        font=("Arial", 20), fg="#fff", anchor="w", bg="#0b032d")
        label.pack(fill="x", padx=10, pady=10)
        
        self.root.mainloop()
passwrodgenerater()
