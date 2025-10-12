import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector

def insertaRegistro (nombre, apellido, edad, estatura, telefono, genero):
    try:
      conexion = mysql.connector.Connect(
          host="localhost", #127.0.0.1
          user="root",
          password="",
          database="programacionavanzada",
          port="3306"
          )
      cursor = conexion.cursor()
      stringQuery = "INSERT INTO registros (Nombre, Apellido, Telefono, Estatura, Edad, Genero) VALUES (%s,%s,%s,%s,%s,%s)"
      valores = nombre, apellido, telefono, estatura, edad, genero
      cursor.execute(stringQuery, valores)
      conexion.commit()
      cursor.close()
      conexion.close()
      messagebox.showinfo("Insercion correcta","Datos gaurdados con exito")

    except mysql.connector.Error as err:
        messagebox.showerror("Error en la conexion en la base de datos,",f"Error al insertar datos: {err}")


def limpiar_campos():
    tbNombre.delete(0,tk.END)
    tbApellido.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)

def borrar_fun():
    limpiar_campos()

def guardar_valores():
    nombre = tbNombre.get()
    apellido = tbApellido.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    genero = ""

    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    # Validar que los campos tengan el formato correcto 
    if (es_entero_valido(edad) and es_decimal_valido(estatura) and es_entero_valido_de_10_digitos(telefono) and 
        es_texto_valido(nombre) and es_texto_valido(apellido)):

            datos = ("Nombres: " + nombre + "\n" + "Apellidos: " + apellido + "\n" + "Edad: " + edad + " anos\n" 
                + "Estatura: " + estatura + "\n" + "Telefono: " + telefono + "\n" + "Genero: " + genero)

            with open ("3O2025.txt","a") as archivo:
                archivo.write(datos + "\n\n")

            insertaRegistro (nombre, apellido, edad, estatura, telefono, genero)
            messagebox.showinfo ("Informacion", "Datos gurdados con exito: \n\n" + datos)

            borrar_fun()
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos validos en los campos.")

def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float (valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

ventana = tk.Tk()
ventana.geometry("300x400")
ventana.title("Formulario Vr.03")

var_genero = tk.IntVar()

lbNombre = tk.Label(ventana, text = "Nombre: ")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()
lbApellido = tk.Label(ventana, text = "Apellido: ")
lbApellido.pack()
tbApellido = tk.Entry()
tbApellido.pack()
lbTelefono = tk.Label(ventana, text = "Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()
lbEdad = tk.Label(ventana, text = "Edad: ")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()
lbEstatura = tk.Label(ventana, text = "Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()
lbGenero =tk.Label(ventana, text = "Genero")
lbGenero.pack()
rbHombre = tk.Radiobutton(ventana, text = "Hombre", variable = var_genero, value = 1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text = "Mujer", variable = var_genero, value = 2)
rbMujer.pack()

btnBorrar = tk.Button(ventana, text = "Borrar valores", command = borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text = "Guardar", command = guardar_valores)
btnGuardar.pack()

ventana.mainloop()
