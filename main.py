from tkinter import *
 
 
class SimpleInterestCalculator:
   def __init__(self, master):
       self.master = master
       master.title("Simple Interest Calculator - The Pycodes")
       master.geometry("500x300")
 
 
       self.principal_label = Label(master, text="Principal:", font="arial 15")
       self.rate_label = Label(master, text="Rate Of Interest:", font="arial 14")
       self.time_label = Label(master, text="Time:", font="arial 15")
 
 
       self.principal_label.place(x=50, y=20)
       self.rate_label.place(x=50, y=90)
       self.time_label.place(x=50, y=160)
 
 
       self.interest_label = Label(master, text="Interest:", font="arial 15")
       self.interest_label.place(x=50, y=230)
 
 
       self.principal_value = StringVar()
       self.rate_value = StringVar()
       self.time_value = StringVar()
 
 
       self.principal_entry = Entry(master, textvariable=self.principal_value, font="arial 20", width=8)
       self.rate_entry = Entry(master, textvariable=self.rate_value, font="arial 20", width=8)
       self.time_entry = Entry(master, textvariable=self.time_value, font="arial 20", width=8)
 
 
       self.principal_entry.place(x=200, y=20)
       self.rate_entry.place(x=200, y=90)
       self.time_entry.place(x=200, y=160)
 
 
       self.result_label = Label(master, text="", font="arial 30 bold")
       self.result_label.place(x=200, y=220)
 
 
       self.calculate_button = Button(master, text="Calculate", font="arial 15", command=self.calculate)
       self.calculate_button.place(x=350, y=20)
 
 
       self.clear_button = Button(master, text="Clear", font="arial 15", command=self.clear_entries)
       self.clear_button.place(x=350, y=90)
 
 
       self.exit_button = Button(master, text="Exit", command=master.destroy, font="arial 15", width=8)
       self.exit_button.place(x=350, y=160)
 
 
   def calculate(self):
       try:
           principal = float(self.principal_value.get())
           rate = float(self.rate_value.get())
           time = float(self.time_value.get())
           amount = (principal * rate * time) / 100
           self.result_label.config(text=f"{amount}")
       except ValueError:
           self.result_label.config(text="Invalid input. Please enter valid numbers.")
 
 
   def clear_entries(self):
       self.principal_value.set("")
       self.rate_value.set("")
       self.time_value.set("")
       self.result_label.config(text="")
 
 
if __name__ == "__main__":
   root = Tk()
   app = SimpleInterestCalculator(root)
   root.mainloop()
