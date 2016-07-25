import tkinter  as tk
from tkinter import ttk
import math as mt
FONT = ("courier new",20)
BTN_FONT = ("courier new", 12)
        
    
def createWidget(container, char, color, w, h,fg, cmd = None, fnt = None):
    widget = tk.Button(container, text = char,
                       width = w, height = h,
                       bg = color,fg = fg, font = fnt, command = cmd)
    return widget

def createFrame(cont, side):
    frame = tk.Frame(cont)
    frame.pack(fill = tk.BOTH, expand = 1, side = side)
    return frame

def parseExp(exp):
    try:
        if('!' in exp):
            return myfactorial(exp)
        ans = eval(exp)
        return ans
    except:
        return "ERROR"

def fib(n):
    try:
        n = int(n)
    except:
        return "ERROR"
    x = 1; y = 1
    if(n > 10000):
        return "Too Big!"
    if(n == 0 or n == 1):
        return n
    for i in range(1,n):
        x, y = y,y + x
    return x

def logMean(x):
    try:
        val = x.split(',')
        x = int(val[0])
        y = int(val[1])
        return ((x-y)/(mt.log(x/y)))
    except:
        return "ERROR"

def myfactorial(n):
    try:
        n = n.lstrip('!').rstrip('!')        
        n = int(n)       
        answer = mt.factorial(n)           
        return answer
    except:
        return "ERROR"

def mylog(n):
    try:
        n = int(n)
        return mt.log(n)
    except:
        return "ERROR"

class Calculator(tk.Tk):
    """
      Calculator class --> parent window for all
      widget
    """
    def __init__(self,*arg, **kwargs):
        tk.Tk.__init__(self,*arg, **kwargs)
        tk.Tk.iconbitmap(self, default = 'abacus.ico')


        self.cont = tk.Frame(self)
        self.cont.pack(fill = tk.BOTH, expand = 1)
        self.cont.grid_columnconfigure(0,weight = 1)
        self.cont.grid_rowconfigure(0, weight = 1)

        self.cont.grid_columnconfigure(1,weight = 1)
        self.cont.grid_rowconfigure(1, weight = 1)

        self.cont.grid_columnconfigure(2,weight = 1)
        self.cont.grid_rowconfigure(2, weight = 1)

        self.cont.grid_columnconfigure(3,weight = 1)
        self.cont.grid_rowconfigure(3, weight = 1)
        
        self.var = tk.StringVar() ## Holds numbers for processing
        
        self.inputBox = tk.Entry(self.cont, textvariable = self.var, relief = tk.RIDGE,
                                borderwidth = 15,background = "sky blue",
                                 foreground = "black", justify = tk.RIGHT,
                                 font = FONT)
        self.inputBox.grid(row = 0,rowspan = 2, columnspan = 4, sticky = "NSWE")
        
        rowNum = 2;
        columNum = 0;
        ## THIS LOOP CREATES THE BUTTONS AND OTHER WIDGETS
        ## ADD MORE CHAR FOR NEW BUTTONS AND CONFIGURE AS
        ## NECESSARY
        for i in ("CLR","FIB","LN","LM","!~%,","789*","456-","123+","0/.="):
            self.shade = "orange"
            self.foreg = "black"
            self.funKeys_color = "#003b6f"

            if(i == "CLR"):
                self.button = createWidget(self.cont, i,self.funKeys_color,
                                           5, 5,self.foreg,
                                      lambda disp = self.var: disp.set(""))
                self.button.grid(row = rowNum, column = columNum, sticky = "NSEW")
                columNum += 1
                continue;
            if(i == "FIB"):
                self.button = createWidget(self.cont, i, self.funKeys_color,
                                           5, 5,self.foreg,
                                      lambda disp = self.var: disp.set(fib(disp.get())))
                self.button.grid(row = rowNum, column = columNum, sticky = "NSEW")
                columNum += 1
                continue;

            if(i == "LN"):
                self.button = createWidget(self.cont, i, self.funKeys_color,
                                           5, 5,self.foreg,
                                      lambda disp = self.var: disp.set(mylog(disp.get())))
                self.button.grid(row = rowNum, column = columNum, sticky = "NSEW")
                columNum += 1
                continue;

            if(i == "LM"):
                self.button = createWidget(self.cont, i,  self.funKeys_color,
                                           5, 5,self.foreg,
                                      lambda disp = self.var: disp.set(logMean(disp.get())))
                self.button.grid(row = rowNum, column = columNum, sticky = "NSEW")
                columNum += 1
                continue;
            
            for char in i:
                if(char in ("-+*%^&$#!~/.=")):
                    self.shade = "black"
                    self.foreg = "white"
                columNum += 1
                if(columNum >= 4):
                    columNum = 0;
                    rowNum += 1;
                    
                if(char == "="):
                    self.button = createWidget(self.cont, char, self.shade, 5, 5, self.foreg,
                                               lambda disp = self.var: disp.set(parseExp(disp.get())),
                                               BTN_FONT)
                    self.button.grid(row = rowNum, column = columNum, sticky = "NSEW")
                    continue;
     
                     
                self.button = createWidget(self.cont, char,self.shade, 5, 5,self.foreg,
                                          lambda disp = self.var, num = char: disp.set(disp.get() + num)
                                           ,BTN_FONT)
                self.button.grid(row = rowNum, column = columNum, sticky = "NSEW")






                
            
        
## STARTS APP     
if __name__ == "__main__":
    app = Calculator()
    app.title("Not So Ordinary Calculator")    
    app.mainloop

