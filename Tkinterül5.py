#tehvan marjapuu
#13.02.24
#TkinterÜl5




import tkinter
from tkinter import Canvas, Entry, IntVar, Radiobutton, ttk

#Koosta pildi järgi käibemaksukalkulaatori programm. Kasutaja sisestab hinna ning valib käibemaksu määra ja sinu programm kuvab eraldi käibemaksu ja hinna koos käibemaksuga.


aken = tkinter.Tk()
aken.title("käibemaksu programm")
aken.geometry("300x200")

vastus = tkinter.Label(aken)  
label = ttk.Label(aken, text="hind käibemaksuta:", font="Tahoma 12", anchor= "w", justify="left")
label.grid(row=0, column=0, columnspan=4)
label = ttk.Label(aken, text="käibemaksumäär:", font="Tahoma 12", anchor= "w", justify="left")
label.grid(row=1, column=0, columnspan=4)


sisestus = Entry(aken)
sisestus.grid(row=0,column=4, columnspan=4)


def naita_valikut():
    print(var.get())


var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=1, command=naita_valikut)
valikukast.grid(row=1, column=4)
valikukast = Radiobutton(aken,text="22%", variable=var, value=2, command=naita_valikut)
valikukast.grid(row=2, column=4)


separator = ttk.Separator(aken, orient='horizontal',).grid(row=3, column=0, columnspan=10, sticky="ew")

vastus= tkinter.Label(aken, text="käibemaks:", font="Tahoma 12", anchor= "w", justify="left")
vastus.grid(row=4, column=0, columnspan=4)

vastus1 = tkinter.Label(aken, text="hind käibemaksuga:", font="Tahoma 12", anchor= "w", justify="left")
vastus1.grid(row=5, column=0, columnspan=4)

def arvuta():
    hind = int(sisestus.get())
    if var.get() == 1:
        vastus.config(text=f"käibemaks: {round(hind*0.09, 2)}")
        vastus1.config(text=f"hind käibemaksuga: {round(hind*1.09, 2)}")
    else:
        vastus.config(text=f"käibemaks: {round(hind*0.22, 2)}")
        vastus1.config(text=f"hind käibemaksuga: {round(hind*1.22, 2)}")    

nupp = ttk.Button(aken, text="arvuta", command=arvuta)
nupp.grid(row=6, column=4)



aken.mainloop()