import tkinter
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox as tkMessageBox
 
def callback():
    pass

class MyGUI:   

    def __init__(self):        
        # create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Body Mass Index Calculator")
        self.main_window.configure(background='aliceblue')
        self.calculated_bmi_value =StringVar()
        self.result_var = StringVar()

        # create a menu
        menu = Menu(self.main_window)
        self.main_window.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Patient", command=callback)
        filemenu.add_command(label="Open Recent", command=callback)
        filemenu.add_separator()
        filemenu.add_command(label="Exit Calculator", command=callback)
        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About Body Mass Index Calculator", command=callback)

        #  create frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window, bg= "aliceblue")
        self.mid_frame = tkinter.Frame(self.main_window, bg= "aliceblue")
        self.bottom_frame = tkinter.Frame(self.main_window, bg= "aliceblue")

        # Top frame
        # create widgets
        self.note_label = tkinter.Label(self.top_frame, text="Note: Enter weight in kilograms(kg) and Height in metres(m).", bg= "aliceblue")
        self.note_label.grid(row=0, columnspan=2, padx=20)

        self.weight_label = tkinter.Label(self.top_frame, bg= "aliceblue", text="Weight: ", justify="left")
        self.weight_label.grid(row=1, column=0)
        self.weight_entry = tkinter.Entry(self.top_frame, font= "bold", width = 10, justify="left")
        self.weight_entry.grid(row=1, column=1)
       
        self.height_label = tkinter.Label(self.top_frame, text="Height: ", bg= "aliceblue", justify="left")
        self.height_label.grid(row=2, column=0)
        self.height_entry = tkinter.Entry(self.top_frame, font= "bold", width = 10, justify="left")
        self.height_entry.grid(row=2, column=1)

        # Middle frame
        # create widgets for mid frame
        self.cal_button = tkinter.Button(self.mid_frame, bg= "sky blue", text = "Calculate", command=self.calculateBMI)
        self.cal_button.grid(row=4, column=0, columnspan=1, pady=10, padx=10, ipadx=30)

        # create reset button for mid frame
        self.reset_button = tkinter.Button(self.mid_frame, bg= "sky blue", text = "Reset", command= self.reset)
        self.reset_button.grid(row=4, column=1, columnspan=1, pady=10, padx=10, ipadx=30)

        # create quit button for mid frame
        self.quit_button = tkinter.Button(self.mid_frame, bg= "sky blue", text = "Quit", command= self.main_window.quit)
        self.quit_button.grid(row=5, columnspan=2, pady=10, padx=10, ipadx=50)

        # Bottom frame
        # create widgets for bottom frame
        self.result_label = tkinter.Label(self.bottom_frame, width = 100,textvariable=self.result_var, bg= "aliceblue", justify="left")
        self.result_label.grid(row=6, columnspan=2, padx=10, pady=10, ipadx= 50, ipady=50)
        
        # call the label widget's pack method
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
    
        # To reset the calculator   
    def reset(self):
        # To clear texboxes
        self.weight_entry.delete (0, END)
        self.height_entry.delete (0, END)          

        # To calculate the BMI
    def calculateBMI(self):
        self.weight_entry.get()
        input_weight = float(self.weight_entry.get())

        self.height_entry.get()
        input_height = float(self.height_entry.get())
        
        height_square = (input_height * input_height)
        body_mass_index = input_weight / height_square
        bmi = round(body_mass_index, 2)
        print(bmi)
        self.calculated_bmi_value.set(bmi)
        self.result_var.set("Your Body Mass Index (BMI) is: " + str(bmi) + ".")
        # tkMessageBox.showinfo("Results", "Your Body Mass Index (BMI) is: " + str(bmi) + ".")  
        if bmi < 18.50:
            tkMessageBox.showwarning("Caution!", "According to your Body Mass Index (BMI), you are underweight.") 
        elif 18.50 >= bmi <=24.90:
            tkMessageBox.showinfo("Congrats!", "According to your Body Mass Index (BMI), you are healthy!") 
        elif 25.00 >= bmi <= 29.90:
            tkMessageBox.showwarning("Caution!", "According to your Body Mass Index (BMI), you are overweight!") 
        else:
            tkMessageBox.showwarning("Caution!", "According to your Body Mass Index (BMI), you are obese!") 

    # def result(self):
    #     # self.result_text = tkMessageBox.showinfo("Results", "Your Body Mass Index (BMI) is: " + str(bmi) + ".")  
    #     self.result_var.set("Your Body Mass Index (BMI) is: " + str(bmi) + ".")

        
my_gui = MyGUI()
            

