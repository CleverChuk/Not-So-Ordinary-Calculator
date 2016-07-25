from tkinter import *
from tkinter import ttk
root = Tk()

# All Button


##input_1 = Button(root, text='1', bg='Orange')
##input_1.grid(row=0, column=0, sticky = "WE", columnspan = 4);
entryBox = Entry(root)
entryBox.grid(row = 0, column = 0, sticky = "WE", columnspan = 4)


button_1 = Button(root, text='1', bg='Orange')
button_1.grid(row=1)

button_4 = Button(root, text='4', bg='Orange')
button_4.grid(row=2)

button_7 = Button(root, text='7', bg='Orange')
button_7.grid(row=3)

button_2 = Button(root, text='2', bg='Orange')
button_2.grid(row=1, column=1)

button_3 = Button(root, text='3', bg='Orange')
button_3.grid(row=1, column=2)

addButton = Button(root, text='+', bg='Orange')
addButton.grid(row=1, column=3)

button_5 = Button(root, text='5', bg='Orange')
button_5.grid(row=2, column=1)

button_6 = Button(root, text='6', bg='Orange')
button_6.grid(row=2, column=2)

subButton = Button(root, text='-', bg='Orange')
subButton.grid(row=2, column=3)

button_8 = Button(root, text='8', bg='Orange')
button_8.grid(row=3, column=1)

button_9 = Button(root, text='9', bg='Orange')
button_9.grid(row=3, column=2)

multiplyButton = Button(root, text='*', bg='Orange')
multiplyButton.grid(row=3, column=3)

button_0 = Button(root, text='0',fg='White', bg='Black')
button_0.grid(row=4, column=0)

Button_equal = Button(root, text='=',fg='white', bg='Black')
Button_equal.grid(row=4, column=3)

divideButton = Button(root, text='/', fg='white', bg='Black')
divideButton.grid(row=4, column=1)

periodButton = Button(root, text='.', fg='white', bg='Black')
periodButton.grid(row=4, column=2)


# Button configurations

button_1.config(height=5, width=6)
button_2.config(height=5, width=6)
button_3.config(height=5, width=6)
button_4.config(height=5, width=6)
button_5.config(height=5, width=6)
button_6.config(height=5, width=6)
button_7.config(height=5, width=6)
button_8.config(height=5, width=6)
button_9.config(height=5, width=6)

addButton.config(height=5, width=6)
subButton.config(height=5, width=6)
multiplyButton.config(height=5, width=6)

button_0.config(height=2, width=6)
Button_equal.config(height=2, width=6)
divideButton.config(height=2, width=6)
periodButton.config(height=2, width=6)

##input_1.config(height=1, width=5, padx=0)
root.resizable(0, 0)

root.mainloop()
