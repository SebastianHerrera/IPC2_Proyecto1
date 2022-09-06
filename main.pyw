import tkinter
from tkinter import filedialog
from tkinter import ttk
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element
##VENTANA

ventana = tkinter.Tk()
ventana.title("Práctica 1")
ventana.resizable(0,0)
ventana.iconbitmap("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab Lenguajes Formales y de Programación/Práctica 1/Programa/logo.ico")
ventana.config(bg="#212F3C")

##FRAME

frame = tkinter.Frame(ventana, width=800, height=500)
ancho_frame= 800
alto_frame= 500
x_frame = frame.winfo_screenwidth()//2-ancho_frame//2
y_frame = frame.winfo_screenheight()//2-alto_frame//2
posicion=str(ancho_frame)+"x"+str(alto_frame)+"+"+str(x_frame)+"+"+str(y_frame)
ventana.geometry(posicion)
frame.config(bg="#212F3C")
frame.pack()

##FRAME PARA GRÁFICAS

frame_para_gráficas = tkinter.Frame(frame, width=500, height=470)
ancho_frame= 20
alto_frame= 15
frame_para_gráficas.config(bg="#2E4053")
frame_para_gráficas.place(x=ancho_frame, y=alto_frame)

##XML Desde archivo

lista=[]
tamaños=[]

def buscar_archivo():
    doc = minidom.parse(nombre_archivo)
    pacientes = doc.getElementsByTagName("paciente")
    for paciente in pacientes:
        nombre = paciente.getElementsByTagName("nombre")[0]
        lista.append(nombre.firstChild.data)
        print("Nombre:%s " % nombre.firstChild.data)
        
    print(lista)


##MÉTODO COMBOBOX
def combo_box():
    global opciones
    opciones= ttk.Combobox(frame,state="readonly", values=lista)
    opciones.place(x=590,y=130)

##BOTON SELECCIONAR PACIENTE

def selec_paciente():
    def guardar_seleccion():
        opciones.get()
        print(opciones.get())
        global nombre_paciente
        nombre_paciente = opciones.get()
    boton_explorar = tkinter.Button(frame, text = "Seleccionar Paciente", command = guardar_seleccion)
    boton_explorar.place(x=600,y=170)  
    boton_explorar.config(bg="#17202A", fg="white", cursor="hand2")

def tamaño():
    doc = minidom.parse(nombre_archivo)
    pacientes = doc.getElementsByTagName("paciente")
    for paciente in pacientes:
        tamaño = paciente.getElementsByTagName("m")[0]
        tamaños.append(tamaño.firstChild.data)
        print("Nombre:%s " % tamaño.firstChild.data)

##MÉTODO CARGAR ARCHIVO

def browseFiles(): 

    filename = filedialog.askopenfilename(initialdir = "C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Práctica 1/Archivos de Entrada"
    , title = "Seleccione un Archivo de Entrada", filetypes = (("Archivos de Datos","*.XML*"),("all files","*.*")))
    print(filename)
    global nombre_archivo
    nombre_archivo = str(filename)
    global state
    state=1
    if state==1:
        buscar_archivo()
        combo_box()
        selec_paciente()
        tamaño()
    else:
        print("Archivo no cargado")


##BOTÓN CARGAR ARCHIVO

boton_explorar = tkinter.Button(frame, text = "Cargar Archivo", command = browseFiles)
boton_explorar.place(x=618,y=70)  
boton_explorar.config(bg="#17202A", fg="white", cursor="hand2")

##MAINLOOP

ventana.mainloop()