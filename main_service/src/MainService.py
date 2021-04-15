import tkinter as tk
import os 
import sys
import urllib.request
from display import DISPLAY

def handle_RStudio(event):
        urllib.request.urlopen("http://localhost:3002/")

def handle_Spyder(event):
        urllib.request.urlopen("http://localhost:3003/")

def handle_IBM_SAS(event):
        urllib.request.urlopen("http://localhost:3004/")

def handle_Git(event):
        urllib.request.urlopen("http://localhost:3001/")

def handle_Jupyter(event):
        urllib.request.urlopen("http://localhost:3005/")

def handle_Orange(event):
        print("orange")

def handle_VS_Code(event):
        print("vs code")

def handle_Hadoop(event):
        

def handle_Spark(event):
        urllib.request.urlopen("http://localhost:3008/")

def handle_Tableau(event):
        urllib.request.urlopen("http://localhost:3010/")

def handle_SonarCloud(event):
        urllib.request.urlopen("http://localhost:3011/")

def handle_Tensorflow(event):
        print("tensorflow")

def handle_Markdown(event):
        print("markdown")

if __name__ == '__main__':
        if os.environ.get('DISPLAY','') == '':
                os.environ.__setitem__('DISPLAY', DISPLAY)
    
        window = tk.Tk()
        window.title('Luke Donnelly Docker Toolbox')
        window.columnconfigure(0, minsize=250)
        window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12], minsize=25) 
        button1 = tk.Button(text="RStudio")
        button1.grid(row=0, column=0)
        button1.bind("<Button-1>", handle_RStudio)      
        button2 = tk.Button(text="Spyder")
        button2.grid(row=1, column=0)
        button2.bind("<Button-1>", handle_Spyder)       
        button3 = tk.Button(text="IBM SAS")
        button3.grid(row=2, column=0)
        button3.bind("<Button-1>", handle_IBM_SAS)

        button4 = tk.Button(text="Git")
        button4.grid(row=3, column=0)
        button4.bind("<Button-1>", handle_Git)

        button5 = tk.Button(text="Jupyter Notebook")
        button5.grid(row=4, column=0)
        button5.bind("<Button-1>", handle_Jupyter)

        button6 = tk.Button(text="Orange")
        button6.grid(row=5, column=0)
        button6.bind("<Button-1>", handle_Orange)

        button7 = tk.Button(text="Visual Studio Code")
        button7.grid(row=6, column=0)
        button7.bind("<Button-1>", handle_VS_Code)

        button8 = tk.Button(text="Apache Hadoop")
        button8.grid(row=7, column=0)
        button8.bind("<Button-1>", handle_Hadoop)

        button9 = tk.Button(text="Apache Spark")
        button9.grid(row=8, column=0)
        button9.bind("<Button-1>", handle_Spark)

        button10 = tk.Button(text="Tableau")
        button10.grid(row=9, column=0)
        button10.bind("<Button-1>", handle_Tableau)

        button11 = tk.Button(text="SonarCloud")
        button11.grid(row=10, column=0)
        button11.bind("<Button-1>", handle_SonarCloud)

        button12 = tk.Button(text="Tensorflow")
        button12.grid(row=11, column=0)
        button12.bind("<Button-1>", handle_Tensorflow)

        button13 = tk.Button(text="Markdown")
        button13.grid(row=12, column=0)
        button13.bind("<Button-3>", handle_Markdown) 

        window.mainloop()