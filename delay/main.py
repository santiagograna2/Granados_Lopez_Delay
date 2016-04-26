#programa que superpone audios delay
#disenado por santiago granados e ismael lopez
#programacion de audio aplicada
#universidad de san buenaventura
from seno import Seno
from openfile import open
from reproducir import Play
from Tkinter import *
from Delay import delay

ventana = Tk()
ventana.title('Suma de audios')
ventana.geometry("600x451")
ventana.configure(bg="white")
imageL=PhotoImage(file="fondoapp.gif")
lblImagen=Label(ventana,image=imageL).place(x=0,y=0)
#imageL=PhotoImage(file="sumaudioimg.gif")
#lblImagen=Label(ventana,image=imageL).place(x=1,y=160)

audio_file_name = ''
audio_file_name2 = ''
Audio1=[]
global primero, segundo
cuadro= Label(ventana, fg="black", padx=15, pady=10, text="Frecuencia:\n (Fq del tono a generar)")
cuadro.pack(side=TOP)
tono=Entry(ventana, bd=5,insertwidth=1)
tono.pack(side=TOP, padx=15, pady=10)
cuadro1= Label(ventana, fg="black", padx=15, pady=10, text="Cuadros:\n (# de frames a retrasar el audio)")
cuadro1.pack(side=TOP)
frames=Entry(ventana, bd=5, insertwidth=1)
frames.pack(side=TOP, padx=15, pady=10)
cuadrob= Label(ventana, fg="black", padx=15, pady=10, text="")
cuadrob.pack(side=TOP)
cuadro3= Label(ventana, fg="black", padx=15, pady=10, text="Tiempo de repeticiones:")
cuadro3.pack(side=TOP)
tiempo=Entry(ventana, bd=5,insertwidth=1)
tiempo.pack(side=TOP, padx=15, pady=10)
cuadro4= Label(ventana, fg="black", padx=15, pady=10, text="Numero de repeticiones:")
cuadro4.pack(side=TOP)
rep=Entry(ventana, bd=5,insertwidth=1)
rep.pack(side=TOP, padx=15, pady=10)
cuadro2= Label(ventana, fg="black", padx=15, pady=10, text="Fase:").place(x=470,y=65)


#tono=Entry(ventana, bd=5, insertwidth=1).place(x=110,y=60)
def porframes():
    h=float(tono.get())
    fram=int(frames.get())
    a=Seno(44100,16,h,fram)

    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()


def pi():
    periodo=1/(float(tono.get()))
    piseg= periodo/2
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)

def pi2():
    periodo=1/(float(tono.get()))
    piseg= periodo/4
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()

def pi4():
    periodo=1/(float(tono.get()))
    piseg= periodo/8
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()
def pi8():
    periodo=1/(float(tono.get()))
    piseg= periodo/16
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()

def archivo():
    import numpy as np
    global Audio
    onda= open()
    Audio=onda.open_masker()
    for i in range (len (Audio)):
        primero=np.asarray(Audio[i])
    print "nuevo",Audio
    return Audio

def sendelay():
    n=int(rep.get())
    t=float(tiempo.get())
    p=delay(Audio,n,t)
    arraydelay=p.generar()
    z=Play(arraydelay)
    y=z.generar()



#tono=Entry(ventana, bd=5, insertwidth=1).place(x=110,y=60)


b1 = Button(ventana,text="Frames",command=porframes ,font=("Agency FB", 14),width=10).place(x=255,y=210)
b2 = Button(ventana,text="Pi",command=pi,font=("Agency FB", 14),width=10).place(x=460,y=95)
b3 = Button(ventana,text="Pi/2",command=pi2,font=("Agency FB", 14),width=10).place(x=460,y=125)
b4 = Button(ventana,text="Pi/4",command=pi4, font=("Agency FB", 14),width=10).place(x=460,y=155)
b5 = Button(ventana,text="Pi/8",command=pi8,font=("Agency FB", 14),width=10).place(x=460,y=185)
b6 = Button(ventana,text="Sel. archivo",command=archivo,font=("Agency FB", 14),width=15).place(x=20,y=340)
b7 = Button(ventana,text="Play Delay",command=sendelay,font=("Agency FB", 14),width=15).place(x=450,y=340)




ventana.mainloop()