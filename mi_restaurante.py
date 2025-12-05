from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [78500, 92000, 189000, 65000, 55000, 58000, 45000, 50000]
precios_bebida = [8000, 12000, 11000, 20000, 175000, 12000, 180000, 14500]
precios_postres = [18000, 10000, 16000, 15000, 12000, 16000, 20000, 13000]


def click_boton(numero):
    global operador
    operador += numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida += (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida += (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres += (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.config(state=NORMAL)
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n')

    texto_recibo.insert(END, f'*' * 53 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, '-' * 60 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'$ {int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, '-' * 60 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, '-' * 60 + '\n')
    texto_recibo.insert(END, f'sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, '*' * 60 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')
    texto_recibo.config(state=DISABLED)


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if archivo:
        archivo.write(info_recibo)
        archivo.close()
        messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetar():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)


    var_costo_comida.set('$ 0.0')
    var_costo_bebida.set('$ 0.0')
    var_costo_postres.set('$ 0.0')
    var_subtotal.set('$ 0.0')
    var_impuestos.set('$ 0.0')
    var_total.set('$ 0.0')

    texto_recibo.config(state=NORMAL)
    texto_recibo.delete(1.0, END)
    texto_recibo.config(state=DISABLED)

    visor_calculadora.delete(0, END)


# Iniciar tkinter
aplicacion = Tk()

# Obtener dimensiones de la pantalla
ancho_pantalla = aplicacion.winfo_screenwidth()
alto_pantalla = aplicacion.winfo_screenheight()

# Calcular posición centrada
ancho_ventana = int(ancho_pantalla * 0.95)
alto_ventana = int(alto_pantalla * 0.90)
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2

aplicacion.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

# Permitir redimensionamiento
aplicacion.resizable(False, False)

# Titulo de la ventana
aplicacion.title('Mi Restaurante - Sistema de facturacion')

# Color de fondo de la ventana
aplicacion.config(bg='burlywood')

# Configurar grid principal
aplicacion.grid_rowconfigure(0, weight=0)
aplicacion.grid_rowconfigure(1, weight=1)
aplicacion.grid_columnconfigure(0, weight=1)

# Panel superior
panel_superior = Frame(aplicacion, bg='burlywood')
panel_superior.grid(row=0, column=0, sticky='ew', pady=10)

etiqueta_titulo = Label(panel_superior,
                        text='Sistema de Facturacion',
                        fg='azure4',
                        font=('Dosis', 48, 'bold'),
                        bg='burlywood')
etiqueta_titulo.pack()

# Panel contenedor principal
panel_contenedor = Frame(aplicacion, bg='burlywood')
panel_contenedor.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

panel_contenedor.grid_rowconfigure(0, weight=1)
panel_contenedor.grid_columnconfigure(0, weight=1)
panel_contenedor.grid_columnconfigure(1, weight=0)

# Panel izquierdo
panel_izquierdo = Frame(panel_contenedor, bg='burlywood')
panel_izquierdo.grid(row=0, column=0, sticky='nsew', padx=5)

panel_izquierdo.grid_rowconfigure(0, weight=1)
panel_izquierdo.grid_rowconfigure(1, weight=0)
panel_izquierdo.grid_columnconfigure(0, weight=1)
panel_izquierdo.grid_columnconfigure(1, weight=1)
panel_izquierdo.grid_columnconfigure(2, weight=1)

# Panel de items
panel_items = Frame(panel_izquierdo, bg='burlywood')
panel_items.grid(row=0, column=0, columnspan=3, sticky='nsew')
panel_items.grid_columnconfigure(0, weight=1)
panel_items.grid_columnconfigure(1, weight=1)
panel_items.grid_columnconfigure(2, weight=1)
panel_items.grid_rowconfigure(0, weight=1)

# Panel comidas
panel_comidas = LabelFrame(panel_items,
                           text='Comida',
                           font=('Dosis', 16, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='azure4',
                           bg='burlywood')
panel_comidas.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
panel_comidas.grid_columnconfigure(0, weight=1)
panel_comidas.grid_columnconfigure(1, weight=0)

# Panel bebidas
panel_bebidas = LabelFrame(panel_items,
                           text='Bebidas',
                           font=('Dosis', 16, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='azure4',
                           bg='burlywood')
panel_bebidas.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
panel_bebidas.grid_columnconfigure(0, weight=1)
panel_bebidas.grid_columnconfigure(1, weight=0)

# Panel Postres
panel_postres = LabelFrame(panel_items,
                           text='Postres',
                           font=('Dosis', 16, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='azure4',
                           bg='burlywood')
panel_postres.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)
panel_postres.grid_columnconfigure(0, weight=1)
panel_postres.grid_columnconfigure(1, weight=0)

# Panel costos
panel_costos = Frame(panel_izquierdo,
                     bd=1,
                     relief=FLAT,
                     bg='azure4',
                     padx=10,
                     pady=10)
panel_costos.grid(row=1, column=0, columnspan=3, sticky='ew', padx=5, pady=5)
panel_costos.grid_columnconfigure(0, weight=1)
panel_costos.grid_columnconfigure(1, weight=1)
panel_costos.grid_columnconfigure(2, weight=1)
panel_costos.grid_columnconfigure(3, weight=1)
panel_costos.grid_columnconfigure(4, weight=1)
panel_costos.grid_columnconfigure(5, weight=1)

# Panel derecha
panel_derecha = Frame(panel_contenedor, bg='burlywood')
panel_derecha.grid(row=0, column=1, sticky='nsew', padx=5)

panel_derecha.grid_rowconfigure(0, weight=0)
panel_derecha.grid_rowconfigure(1, weight=1)
panel_derecha.grid_rowconfigure(2, weight=0)
panel_derecha.grid_columnconfigure(0, weight=1)

# Panel calculadora
panel_calculadora = Frame(panel_derecha,
                          bd=2,
                          relief=GROOVE,
                          bg='white',
                          padx=10,
                          pady=10)
panel_calculadora.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
panel_calculadora.grid_columnconfigure(0, weight=1)
panel_calculadora.grid_columnconfigure(1, weight=1)
panel_calculadora.grid_columnconfigure(2, weight=1)
panel_calculadora.grid_columnconfigure(3, weight=1)

# Panel recibo
panel_recibo = Frame(panel_derecha,
                     bd=2,
                     relief=GROOVE,
                     bg='white')
panel_recibo.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
panel_recibo.grid_rowconfigure(0, weight=1)
panel_recibo.grid_columnconfigure(0, weight=1)

# Panel botones
panel_botones = Frame(panel_derecha, bg='burlywood')
panel_botones.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
panel_botones.grid_columnconfigure(0, weight=1)
panel_botones.grid_columnconfigure(1, weight=1)
panel_botones.grid_columnconfigure(2, weight=1)
panel_botones.grid_columnconfigure(3, weight=1)

# Lista de productos
lista_comidas = ['Pollo', 'Cerdo', 'Langosta', 'Arroz', 'Milanesa', 'Pizza', 'Salchipapa', 'Hamburguesa']
lista_bebidas = ['Cola', 'Agua', 'Jugo', 'Limonada', 'Vino', 'Cerveza', 'Champaña', 'Avena']
lista_postres = ['Helado', 'Cafe', 'Brownies', 'Gelatina', 'Oblea', 'Merengue', 'Cocada', 'Buñuelo']

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []

for contador, comida in enumerate(lista_comidas):
    variables_comida.append(IntVar())
    check = Checkbutton(panel_comidas,
                        text=comida.title(),
                        font=('Dosis', 12, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variables_comida[contador],
                        bg='burlywood',
                        command=revisar_check)
    check.grid(row=contador, column=0, sticky='w', pady=3)

    texto_comida.append(StringVar())
    texto_comida[contador].set('0')
    cuadros_comida.append(Entry(panel_comidas,
                                font=('Dosis', 10, 'bold'),
                                bd=1,
                                width=5,
                                state=DISABLED,
                                textvariable=texto_comida[contador]))
    cuadros_comida[contador].grid(row=contador, column=1, padx=5, pady=3)

# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

for contador, bebida in enumerate(lista_bebidas):
    variables_bebida.append(IntVar())
    check = Checkbutton(panel_bebidas,
                        text=bebida.title(),
                        font=('Dosis', 12, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variables_bebida[contador],
                        bg='burlywood',
                        command=revisar_check)
    check.grid(row=contador, column=0, sticky='w', pady=3)

    texto_bebida.append(StringVar())
    texto_bebida[contador].set('0')
    cuadros_bebida.append(Entry(panel_bebidas,
                                font=('Dosis', 10, 'bold'),
                                bd=1,
                                width=5,
                                state=DISABLED,
                                textvariable=texto_bebida[contador]))
    cuadros_bebida[contador].grid(row=contador, column=1, padx=5, pady=3)

# Generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []

for contador, postres in enumerate(lista_postres):
    variables_postres.append(IntVar())
    check = Checkbutton(panel_postres,
                        text=postres.title(),
                        font=('Dosis', 12, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variables_postres[contador],
                        bg='burlywood',
                        command=revisar_check)
    check.grid(row=contador, column=0, sticky='w', pady=3)

    texto_postres.append(StringVar())
    texto_postres[contador].set('0')
    cuadros_postres.append(Entry(panel_postres,
                                 font=('Dosis', 10, 'bold'),
                                 bd=1,
                                 width=5,
                                 state=DISABLED,
                                 textvariable=texto_postres[contador]))
    cuadros_postres[contador].grid(row=contador, column=1, padx=5, pady=3)

# Variables de costos
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# Inicializar variables
var_costo_comida.set('$ 0.0')
var_costo_bebida.set('$ 0.0')
var_costo_postres.set('$ 0.0')
var_subtotal.set('$ 0.0')
var_impuestos.set('$ 0.0')
var_total.set('$ 0.0')

# Etiquetas y campos de costos
etiqueta_costo_comida = Label(panel_costos, text='Costo comida', font=('Dosis', 10, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
texto_costo_comida = Entry(panel_costos, font=('Dosis', 10, 'bold'), bd=1, state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

etiqueta_costo_bebida = Label(panel_costos, text='Costo bebida', font=('Dosis', 10, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
texto_costo_bebida = Entry(panel_costos, font=('Dosis', 10, 'bold'), bd=1, state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

etiqueta_costo_postres = Label(panel_costos, text='Costo Postres', font=('Dosis', 10, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postres.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
texto_costo_postres = Entry(panel_costos, font=('Dosis', 10, 'bold'), bd=1, state='readonly',
                            textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, sticky='ew', padx=5, pady=5)

etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=('Dosis', 10, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2, sticky='ew', padx=5, pady=5)
texto_subtotal = Entry(panel_costos, font=('Dosis', 10, 'bold'), bd=1, state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, sticky='ew', padx=5, pady=5)

etiqueta_impuestos = Label(panel_costos, text='Impuestos', font=('Dosis', 10, 'bold'), bg='azure4', fg='white')
etiqueta_impuestos.grid(row=1, column=2, sticky='ew', padx=5, pady=5)
texto_impuestos = Entry(panel_costos, font=('Dosis', 10, 'bold'), bd=1, state='readonly', textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, sticky='ew', padx=5, pady=5)

etiqueta_total = Label(panel_costos, text='Total', font=('Dosis', 10, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2, sticky='ew', padx=5, pady=5)
texto_total = Entry(panel_costos, font=('Dosis', 10, 'bold'), bd=1, state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3, sticky='ew', padx=5, pady=5)

# Visor de calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 14, 'bold'),
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4, sticky='ew', pady=5)

# Botones de calculadora
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', '⌫', '0', '/']
botones_guardados = []

fila = 1
columna = 0

for boton_texto in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton_texto,
                   font=('Dosis', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1)
    boton.grid(row=fila, column=columna, sticky='nsew', padx=2, pady=2)
    botones_guardados.append(boton)

    columna += 1
    if columna == 4:
        columna = 0
        fila += 1

# Configurar pesos para botones de calculadora
for i in range(4):
    panel_calculadora.grid_columnconfigure(i, weight=1)

# Asignar comandos a botones de calculadora
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# Area de recibo con scrollbar
scrollbar = Scrollbar(panel_recibo)
scrollbar.grid(row=0, column=1, sticky='ns')

texto_recibo = Text(panel_recibo,
                    font=('Dosis', 9, 'bold'),
                    bd=1,
                    yscrollcommand=scrollbar.set)
texto_recibo.grid(row=0, column=0, sticky='nsew')
scrollbar.config(command=texto_recibo.yview)
texto_recibo.config(state=DISABLED)

# Botones de control
botones_control = ['Total', 'Recibo', 'Guardar', 'Resetar']

for i, nombre_boton in enumerate(botones_control):
    boton = Button(panel_botones,
                   text=nombre_boton,
                   font=('Dosis', 11, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1)
    boton.grid(row=0, column=i, sticky='nsew', padx=3, pady=5)

    if i == 0:
        boton.config(command=total)
    elif i == 1:
        boton.config(command=recibo)
    elif i == 2:
        boton.config(command=guardar)
    elif i == 3:
        boton.config(command=resetar)

# Evitar que la pantalla se cierre
aplicacion.mainloop()