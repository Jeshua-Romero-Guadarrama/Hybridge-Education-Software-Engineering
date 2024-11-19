import os
import sys
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Calculadora")

# Cambiar ícono de la app
ruta_icono = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Calculadora.ico")
ventana.iconbitmap(ruta_icono)

# Variable para almacenar la expresión matemática
expresion = ""

# Variable para almacenar el estado del visor
resultado_mostrado = False

# Función para actualizar la expresión en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion, resultado_mostrado

    # Evaluar si ya sea ha calculado y mostrado un resultado
    if resultado_mostrado:
        # Evaluar si se presionó un número o ".", reiniciar el visor
        if tecla.isdigit() or tecla == '.':
            expresion = str(tecla)
        else:
            expresion += str(tecla)
        resultado_mostrado = False
    else:
        expresion += str(tecla)
    visor_texto.set(expresion)

# Función para limpiar la entrada
def limpiar():
    global expresion, resultado_mostrado

    expresion = ""
    visor_texto.set(expresion)
    resultado_mostrado = False

# Función para evaluar la expresión y mostrar el resultado
def evaluar():
    global expresion, resultado_mostrado

    try:
        resultado = eval(expresion)
        # Verificar si el resultado es un numero entero
        if resultado == int(resultado):
            resultado = int(resultado)
        visor_texto.set(str(resultado))
        expresion = str(resultado)
        resultado_mostrado = True
    except:
        visor_texto.set("Error")
        expresion = ""
        resultado_mostrado = False

# Configurar el tamaño dinámico de las columnas y filas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Cuadro de texto para mostrar las expresiones y resultado
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 32, 'bold'),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=2,
                 justify='right',
                 relief="sunken",
                 bg="#e8f0fe",
                 fg="#333333")
visor.grid(row=0,
           column=0,
           columnspan=4,
           sticky="ew",
           padx=10,
           pady=10)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# Colores almacenados en variables
color_fondo_numero = '#b3cde0'
color_fondo_operacion = '#7A869A'
color_fondo_especial = '#9B90B6'
color_fondo_calcular = '#b0e57c'
color_fondo_presionado = '#6a51a3'
color_fondo_calcular_presionado = '#76c7c0'
color_texto_numero = '#333333'
color_texto_especial = '#ffffff'

# Crear y posicionar los botones (excepto "=")
for (texto, fila, columna) in botones:
    if texto in ['/', '*', '-', '+']:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial
    elif texto == 'C':
        comando = limpiar
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    elif texto == '.':
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    else:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_numero
        color_texto = color_texto_numero

    tk.Button(ventana,
              text=texto,
              padx=20,
              pady=20,
              font=('Helvetica', 20, 'bold'),
              command=comando,
              bd=1,
              relief="raised",
              bg=color_fondo,
              fg=color_texto,
              activeforeground=color_texto_especial,
              activebackground=color_fondo_presionado
              ).grid(row=fila,
                     column=columna,
                     sticky='nsew',
                     padx=2,
                     pady=2)

# Botón de igual "=" que ocupa toda la ultima fila
tk.Button(ventana,
          text="=",
          padx=20,
          pady=20,
          font=('Helvetica', 40, 'bold'),
          command=evaluar,
          bd=1,
          relief="raised",
          bg=color_fondo_calcular,
          fg=color_texto_numero,
          activeforeground=color_fondo_calcular_presionado,
          activebackground=color_texto_especial
          ).grid(row=5,
                 column=0,
                 columnspan=4,
                 sticky='ew',
                 padx=2,
                 pady=2)

# Ejecutar la aplicación
ventana.mainloop()