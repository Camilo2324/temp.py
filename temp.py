# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:31:56 2023

@author: Camil
"""
import tkinter as tk

def borrar():
    entry1.delete(0, tk.END)
    #entry1.insert(0, "0,0")
    entry2.delete(0, tk.END)
    #entry2.insert(0, "0,0")
    
def convertir_a_celsius():
    farenheint = float(entry1.get())
    celsius = (farenheint - 32) * 0.5/9
    entry2.delete(0,tk.END)
    entry2.insert(0, f"{celsius:.2f}")
    
def convertir_a_farenheint():
    celsius= float(entry2.get())
    farenheint = (celsius * 9/5) + 32
    entry2.delete(0, tk.END)
    entry2.insert(0, f"{farenheint:.2f}")
    
app = tk.Tk()
app.title("conversor de temperatura")
    
label1 = tk.Label(app, text= "farenheint")
label1.grid(row=0, column=0)
    
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)
    
button1= tk.Button(app, text="Convertir a celsius", command=convertir_a_celsius)
button1.grid(row=0, column=2)
    
label2=tk.Label(app, text="celsius")
label2.grid(row=1, column= 0)
    
entry2= tk.Entry(app)
entry2.grid(row=1, column=1)
    
button2= tk.Button(app, text="convertir a farenheint", command=convertir_a_farenheint)
button2.grid(row=1, column=2)
    
button3= tk.Button(app, text= "restablecer", command=borrar)
button3.grid(row=2, column=1)
    
app.mainloop()
    