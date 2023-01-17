import tkinter as tk
from tkinter import font, ttk
from tkinter import *
#Apariencia de la ventana
ventana = tk.Tk()
ventana.title("Reconocimiento de emociones") #Texto que aparece arriba
ventana.geometry("1300x690")
ventana.resizable(width=True, height=True)
ventana.iconbitmap("logo.ico") #Icono de la escuela que aparece en la esquina
#Fondos--------------------------------------------------------------------------------------------------------------------------------
mainFrame=Frame(ventana)
mainFrame.pack()
mainFrame.config(width=1400,height=690,bg="lightblue")
fondo=tk.PhotoImage(file="Entrada.png")
fondo1= tk.Label(mainFrame, image=fondo).place(x=0, y=0, relwidth=1, relheight=1) #Imagen de fondo
#Cuadros de texto para que el usuario escriba
NombreTexto = ttk.Entry(font=font.Font(family="Comic Sans MS", size=14)) #Cuadro de texto de usuario
NombreTexto.place(x=560, y=235) #donde se ubica
ContraseñaTexto = ttk.Entry(show="*", font=font.Font(family="Comic Sans MS", size=14)) # Mostrar asteriscos en lugar del texto original.
ContraseñaTexto.place(x=560, y=265)#donde se ubica
# Texto en la entrada------------------------------------------------------------------------------------------------------------------
Ingresa = Label(mainFrame, text="Ingresa tus datos, porfavor:")#Etiqueta "Ingresa"
Ingresa.config(font=("Comic Sans MS",19))#Tipo de letra
Ingresa.place(x=500, y=175)#donde se ubica
usuario = Label(mainFrame, text="Usuario:")#Etiqueta "Usuario"
usuario.config(font=("Comic Sans MS",14))#Tipo de letra
usuario.place(x=420, y=235)#donde se ubica
contra = Label(mainFrame, text="Contraseña:")#Etiqueta "Contraseña"
contra.config(font=("Comic Sans MS",14))#Tipo de letra
contra.place(x=420, y=265)#donde se ubica
Registra = Label(mainFrame, text="Si no tienes  una cuenta, registrate")#Etiqueta "Registra"
Registra.config(font=("Comic Sans MS",19))#Tipo de letra
Registra.place(x=470, y=380)#donde se ubica
#Botones-------------------------------------------------------------------------------------------------------------------------------
Entrar = ttk.Button(text="Entrar")
Entrar.place(x=650, y=330)
Regist = ttk.Button(text="Registrarse")
Regist.place(x=650, y=470)

ventana.mainloop()