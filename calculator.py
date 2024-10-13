import tkinter as tk

#Instantiating the global variable
calculation = ""

#This function will add all that i'm evaluating into one global variable
def theProblem(symbol):
    global calculation

    calculation += str(symbol)

    textBox.delete(1.0, "end")
    textBox.insert(1.0, calculation)

#This function will evaluate the problem through the eval() function
def evalProblem():
    global calculation

    #Using a try function since there will sometimes be errors
    try:
        calculation = str(eval(calculation))
        textBox.delete(1.0, "end")
        textBox.insert(1.0, calculation)
    except:
        clearField()
        textBox.insert(1.0, "Error")


#This function will clear the text box field
def clearField():
    global calculation

    calculation = ""

    textBox.delete(1.0, "end")


#This starts the Tkinter object ----------------------------
root = tk.Tk()

#Creating the size of the calculator
root.geometry("300x275")

#Creating a text box to display the results/the inputs
textBox = tk.Text(root, height=2, width=16, font=("Roboto", 24))
textBox.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: theProblem(1), width=5, font=("Roboto", 14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: theProblem(2), width=5, font=("Roboto", 14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: theProblem(3), width=5, font=("Roboto", 14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: theProblem(4), width=5, font=("Roboto", 14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: theProblem(5), width=5, font=("Roboto", 14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: theProblem(6), width=5, font=("Roboto", 14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: theProblem(7), width=5, font=("Roboto", 14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: theProblem(8), width=5, font=("Roboto", 14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: theProblem(9), width=5, font=("Roboto", 14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: theProblem(0), width=5, font=("Roboto", 14))
btn0.grid(row=5, column=2)

btnPlus = tk.Button(root, text="+", command=lambda: theProblem("+"), width=5, font=("Roboto", 14))
btnPlus.grid(row=2, column=4)
btnMinus = tk.Button(root, text="-", command=lambda: theProblem("-"), width=5, font=("Roboto", 14))
btnMinus.grid(row=3, column=4)
btnMulti = tk.Button(root, text="*", command=lambda: theProblem("*"), width=5, font=("Roboto", 14))
btnMulti.grid(row=4, column=4)
btnDiv = tk.Button(root, text="/", command=lambda: theProblem("/"), width=5, font=("Roboto", 14))
btnDiv.grid(row=5, column=4)

btnLParen = tk.Button(root, text="(", command=lambda: theProblem("("), width=5, font=("Roboto", 14))
btnLParen.grid(row=5, column=1)
btnRParen = tk.Button(root, text=")", command=lambda: theProblem(")"), width=5, font=("Roboto", 14))
btnRParen.grid(row=5, column=3)

btnClear = tk.Button(root, text="AC", command=clearField, width=11, font=("Roboto", 14))
btnClear.grid(row=6, column=1, columnspan=2)
btnEquals = tk.Button(root, text="=", command=evalProblem, width=11, font=("Roboto", 14))
btnEquals.grid(row=6, column=3, columnspan=2)




#This ends the Tkinter main loop ---------------------------
root.mainloop()