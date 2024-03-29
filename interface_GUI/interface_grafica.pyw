from tkinter import *

raiz=Tk()

raiz.title("Ventana")

#raiz.resizable(0,0)

raiz.iconbitmap(r"C:\Users\ARcade\Documents\Cursos de Programacion\Academia Cimne Iber - Python\Practicos\interface_GUI\hambur.ico")

#raiz.geometry("440x230")

raiz.config(bg="orange")

miFrame= Frame()

#miFrame.pack(side="right",anchor="n")

#miFrame.pack(fill="x")

miFrame.pack(fill="y", expand=1)

miFrame.config(bg="red",width="440",height="230")

raiz.mainloop()

