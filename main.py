import tkinter as tk
import random
import string
class passwrodgenerater:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("420x520")
        self.root.config(bg="#0b032d")

        # label name
        self.label=tk.Label(self.root, text="Password Generator", 
        font=("Times New Roman", 20), fg="#fff", anchor="w", bg="#0b032d")
        self.label.pack(fill="x", padx=10, pady=10)
        
        # result box
        self.result_box=tk.Entry(self.root, width=48,justify='center',  readonlybackground="#0b032d", fg="#fff")
        self.result_box.pack(ipady=8, pady=5)
        self.result_box.config(state='normal')
        self.result_box.insert(0, "CLICK GENERATE")
        self.result_box.config(state="readonly", font=("Times New Roman", 12))


        # set length of password
        self.length_var = tk.StringVar(value="LENGTH: 16")
        self.pass_length=16
        self.length_label = tk.Label(self.root, textvariable=self.length_var, 
                                     font=("Arial", 10, "bold"), bg="#0b032d", fg="#777")
        self.length_label.pack(anchor="w", padx=40)

        # The 'command' calls self.update_length every time the slider moves
        self.slider = tk.Scale(self.root, from_=4, to=32, orient="horizontal", 
                               bg="#0b032d", fg="#fff", highlightthickness=0,
                               troughcolor="#161b33", command=self.update_length)
        self.slider.set(16)
        self.slider.pack(fill="x", padx=40, pady=(0, 20))

         # --- Settings Section ---
        tk.Label(self.root, text="SETTINGS", font=("Arial", 9, "bold"), 
                 bg="#0b032d", fg="#777").pack(anchor="w", padx=40, pady=5)

        #Creates a row with a label and a toggle-style checkbox
        
        option=["Uppercase", "Lowercase", "Numbers", "Symbol"]
        self.all_val={}
        for name in option:
            value = self.create_option(name)

            self.all_val[name] = value


         # Generate Button
        self.gen_btn = tk.Button(self.root, text="GENERATE PASSWORD", bg="#6c63ff", 
                                 fg="white", font=("Arial", 11, "bold"), 
                                 relief="flat", pady=10, cursor="hand2", command=self.generatePassword)
        self.gen_btn.pack(fill="x", padx=40, pady=30)
        
        self.root.mainloop()
      
        

    def changeState(self):
        print("Current States:\n")

        for name, var in self.all_val.items():

            print(name, "=", var.get())

        print("----------------")
    def update_length(self, value):
        self.length_var.set(f"LENGTH: {value}")
        self.pass_length=value
    def create_option(parient,text):
        frame = tk.Frame(parient.root, bg="#0b032d")   
        frame.pack(fill='x', padx=40, pady=5)
        check_var =tk.IntVar()
        tk.Label(frame, fg="#fff", text="Include " +text,bg="#0b032d", font=("Arial", 10)).pack(side="left")
        cb = tk.Checkbutton(frame, bg="#0b032d", activebackground="#0b032d", 
                            selectcolor="#161b33", bd=0, variable=check_var, command=parient.changeState)
        cb.pack(side="right", pady=2, anchor='w')
        return check_var
       
    def generatePassword(self):
        lis=[0,1,2,3,4,5,6,7,8,9]
        password =''
        for i in range(int(self.pass_length)):
            choice=random.randint(1,4)
            no=random.randint(1,9)
            chL=random.choice(string.ascii_lowercase)
            chU=random.choice(string.ascii_uppercase)
            chS=random.choice(string.punctuation)
            if choice==1:
                password=password+str(no)
            if choice==2:
                password=password+str(chL)
            if choice==3:
                password=password+str(chU)
            if choice==4:
                password=password+str(chS)
        self.changepasswrod(password)
    def changepasswrod(self, passw):
        self.result_box.config(state='normal',justify='center',  bg="#0b032d", fg="#fff")
        self.result_box.delete(0,tk.END)
        self.result_box.insert(0, passw)
passwrodgenerater()
  