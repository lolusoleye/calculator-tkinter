import tkinter 
import math

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) 
column_count = len(button_values[0])


colour_light_gray = "#DFD4D2"
colour_black = "#1C1C1C"
colour_dark_grey = "#505050"
colour_orange = "#FF9500"
colour_white = "white"



#window setup 
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False,False) 

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "0", font =("Arial",45), background=colour_black,foreground=colour_white,anchor = "e", width = column_count)


label.grid(row=0, column=0,columnspan=column_count,sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button =tkinter.Button(frame, text= value , font =("Arial",30), width = column_count - 1, height= 1, command=lambda value=value: button_clicked(value))

        if value in top_symbols:
            button.config(foreground=colour_black, background=colour_light_gray)
        elif value in right_symbols:
            button.config(foreground=colour_white, background= colour_orange)
        else:
            button.config(foreground=colour_white, background=colour_dark_grey)
        button.grid(row= row+1, column=column)


frame.pack()

#operations go here

A="0"

operator = None
B = None

def clear_all():
    global A,B, operator
    A = "0"
    operator = None
    B = None


def remove_zerodecimal(num):
    if num%1 == 0:
        num = int(num)
    return str(num)

def format_number(num):
    # Round to 3 decimal places
    num = round(num, 3)
    
    # If it's actually an integer (like 12.0), show as int
    if num.is_integer():
        return str(int(num))
    else:
        return str(num)





def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)


                if operator =="+":
                    label["text"] = remove_zerodecimal(numA + numB)
                elif operator =="-":
                    label["text"] = remove_zerodecimal(numA - numB)
                elif operator =="×":
                    label["text"] = remove_zerodecimal(numA * numB)
                elif operator =="÷":
                    label["text"] = remove_zerodecimal(numA / numB)

                clear_all()
        elif value in "+-×÷": #
            if operator == None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            
            operator = value



    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"])  * -1
            label["text"] = remove_zerodecimal(result)
            
        elif value == "%":
            result = float(label["text"]) / 100 
            label["text"] = remove_zerodecimal(result)
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zerodecimal(result)
        elif value == "%":
            result = float(label["text"]) / 100 
            label["text"] = remove_zerodecimal(result) 

    elif value == "√":   # ✅ new square root logic
        num = float(label["text"])
        if num < 0:
            label["text"] = "Error"  # can't sqrt negative
        else:
            result = math.sqrt(num)
            label["text"] = remove_zerodecimal(result)

    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
                if label["text"] == "0":
                    label["text"] = value
                else:
                    label["text"] += value 
    
    



#center window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width =  window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()
