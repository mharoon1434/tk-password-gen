import tkinter as tk

class passwrodgenerater:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("420x520")
        self.root.config(bg="#0b032d")

        # label name
        label=tk.Label(self.root, text="Password Generator", 
        font=("Times New Roman", 20), fg="#fff", anchor="w", bg="#0b032d")
        label.pack(fill="x", padx=10, pady=10)
        
        # result box
        result_box=tk.Entry(self.root, width=48,justify='center',  readonlybackground="#0b032d", fg="#fff")
        result_box.pack(ipady=8, pady=20)
        result_box.config(state='normal')
        result_box.insert(0, "CLICK GENERATE")
        result_box.config(state="readonly", font=("Times New Roman", 12))
        self.root.mainloop()
passwrodgenerater()
