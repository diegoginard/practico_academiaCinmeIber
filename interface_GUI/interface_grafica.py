from tkinter import *

raiz=Tk()

raiz.title("Ventana")

raiz.config(bg="#5DADE2",width="640",height="480",bd=35 ,relief="sunken",cursor="pirate")

#raiz.resizable(0,0)

raiz.iconbitmap(r"C:\Users\ARcade\Documents\Cursos de Programacion\Academia Cimne Iber - Python\Practicos\interface_GUI\hambur.ico")

#raiz.geometry("440x230")

#raiz.config(bg="orange")

miFrame= Frame()

miFrame.pack()

#miFrame.pack(fill="x", expand=True)

miFrame.config(bg="#F8C471",width="500",height="300",cursor="hand2")

cuadroTexto = Entry(miFrame)
cuadroTexto.place(x=120,y=100)

miLabel= Label(miFrame, text= "soy un label: ",bg="#F8C471")
miLabel.place(x=40,y=100)


"""
miBoton = Button(miFrame,text= "soy un boton",bg= "#0B5345",font=("courier",10),fg="red")
miBoton.place(x=70,y=85)
miBoton.pack()
miLabel.place(x=50, y=50)
"""


raiz.mainloop()

