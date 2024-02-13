import tkinter as tk
from tkinter import ttk


aken = tk.Tk()
aken.geometry('200x200')
font = ('Tahoma', 12)
aken.title("kalkulaator")
label = ttk.Label(aken, text="Siia kunagi vastus!", font="Tahoma 12")
label.grid(row=0, column=0, columnspan=4)
aken.resizable(0, 0)

#tegin ühe rea valmis ja siis copy paste kuna kõik nupude kood on sama
button1 = ttk.Button(aken, text='7', width=4)
button1.grid(row=1, column=0, padx=2, pady=2)

button2 = ttk.Button(aken, text='8', width=4)
button2.grid(row=1, column=1, padx=2, pady=2)

button3 = ttk.Button(aken, text='9', width=4)
button3.grid(row=1, column=2, padx=2, pady=2)

button4 = ttk.Button(aken, text='/', width=4)
button4.grid(row=1, column=3, padx=2, pady=2)


button5 = ttk.Button(aken, text='4', width=4)
button5.grid(row=2, column=0, padx=2, pady=2)

button6 = ttk.Button(aken, text='5', width=4)
button6.grid(row=2, column=1, padx=2, pady=2)

button7 = ttk.Button(aken, text='6', width=4)
button7.grid(row=2, column=2, padx=2, pady=2)

button8 = ttk.Button(aken, text='*', width=4)
button8.grid(row=2, column=3, padx=2, pady=2)


button9 = ttk.Button(aken, text='1', width=4)
button9.grid(row=3, column=0, padx=2, pady=2)

button10 = ttk.Button(aken, text='2', width=4)
button10.grid(row=3, column=1, padx=2, pady=2)

button11 = ttk.Button(aken, text='3', width=4)
button11.grid(row=3, column=2, padx=2, pady=2)

button12 = ttk.Button(aken, text='-', width=4)
button12.grid(row=3, column=3, padx=2, pady=2)


button13 = ttk.Button(aken, text='0', width=4)
button13.grid(row=4, column=0, padx=2, pady=2)

button14 = ttk.Button(aken, text=',', width=4)
button14.grid(row=4, column=1, padx=2, pady=2)

button15 = ttk.Button(aken, text='=', width=4)
button15.grid(row=4, column=2, padx=2, pady=2)

button16 = ttk.Button(aken, text='+', width=4)
button16.grid(row=4, column=3, padx=2, pady=2)

aken.mainloop()