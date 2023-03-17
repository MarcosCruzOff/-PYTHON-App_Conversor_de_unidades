from tkinter import *
from tkinter import messagebox

#Funções do app
def check_campos():
    if input_medidas.get() == "None":
        messagebox.showwarning("Aviso","Faça sua escolha primeiro")
    elif input_valores.get() == "":
        messagebox.showwarning("Aviso","Insira algum valor primeiro")
    else : 
       return True
   

def converter():
    if check_campos() == True:
        if input_medidas.get() == "mg":
            valor = int(input_valores.get())
            resultado_1 = round(valor / 1000, 2)           
            resultado_2 = round(valor / 1000000, 2)
                            
            result_1["text"] = f"{resultado_1}g"
            result_2["text"] = f"{resultado_2}kg"
            
        elif input_medidas.get() == "g":
            valor = input_valores.get()
            resultado_1 = round(valor * 1000, 2)           
            resultado_2 = round(valor / 1000, 2)
                            
            result_1["text"] = f"{resultado_1}mg"
            result_2["text"] = f"{resultado_2}kg"
            
        elif input_medidas.get() == "kg":
            valor = input_valores.get()
            resultado_1 = round(valor * 1000000, 2)           
            resultado_2 = round(valor * 1000, 2)
                            
            result_1["text"] = f"{resultado_1}mg"
            result_2["text"] = f"{resultado_2}g"
        elif input_medidas.get() == "g":
            valor = input_valores.get()
            resultado_1 = round(valor * 1000, 2)           
            resultado_2 = round(valor / 1000, 2)
                            
            result_1["text"] = f"{resultado_1}mg"
            result_2["text"] = f"{resultado_2}kg"
            
        elif input_medidas.get() == "kg":
            valor = input_valores.get()
            resultado_1 = round(valor * 1000000, 2)           
            resultado_2 = round(valor * 1000, 2)
                            
            result_1["text"] = f"{resultado_1}mg"
            result_2["text"] = f"{resultado_2}g"
            
        elif input_medidas.get() == "cm":
            valor = input_valores.get()
            resultado_1 = round(valor / 100, 2)           
            resultado_2 = round(valor / 100000, 2)
                            
            result_1["text"] = f"{resultado_1}m"
            result_2["text"] = f"{resultado_2}km"
            
        elif input_medidas.get() == "m":
            valor = input_valores.get()
            resultado_1 = round(valor * 100, 2)           
            resultado_2 = round(valor / 1000, 2)
                            
            result_1["text"] = f"{resultado_1}cm"
            result_2["text"] = f"{resultado_2}km"
            
        elif input_medidas.get() == "km":
            valor = input_valores.get()
            resultado_1 = round(valor * 100000, 2)           
            resultado_2 = round(valor * 1000, 2)
                            
            result_1["text"] = f"{resultado_1}cm"
            result_2["text"] = f"{resultado_2}m"
        
        elif input_medidas.get() == "seg":
            valor = input_valores.get()
            resultado_1 = round(valor / 60, 2)           
            resultado_2 = round(valor / 3600, 2)
                            
            result_1["text"] = f"{resultado_1}min"
            result_2["text"] = f"{resultado_2}hora"
            
        elif input_medidas.get() == "min":
            valor = input_valores.get()
            resultado_1 = round(valor * 60, 2)           
            resultado_2 = round(valor / 60, 2)
                            
            result_1["text"] = f"{resultado_1}seg"
            result_2["text"] = f"{resultado_2}hora"
            
        elif input_medidas.get() == "h":
            valor = input_valores.get()
            resultado_1 = round(valor * 3600, 2)           
            resultado_2 = round(valor * 60, 2)
                            
            result_1["text"] = f"{resultado_1}seg"
            result_2["text"] = f"{resultado_2}min"       
        
        else:
            messagebox.showerror("Fudeo","Teu Pc vai explodir")
    

# Função que filtra a entrada do usuário para permitir apenas números e ponto decimal
def numeric_filter(value):
    if value.isdigit() or value == "" or value == ".":
        if input_campo.index(INSERT) == 0 and value == ".":
            input_campo.insert(INSERT, "0.")
            return False
        elif "." in input_campo.get() and value == ".":
            return False
        elif value == "":
            return True
        elif len(input_campo.get().split(".")[0]) < 3 or input_campo.index(INSERT) > len(input_campo.get()) - 3:
            return True
    return False

# Função que formata um valor float com duas casas decimais e vírgulas a cada três dígitos inteiros
def format_value(value):
    return "{:,.2f}".format(value)









#cores
bg1 = "#121212"
bg2 = "#151515"
fontcor = "#f3f3f3"
txt = "jetBrains Mono"

#configuração base do app
app = Tk()
app.title("App - Conversor de Medidas")
app.geometry("500x400")
app.resizable(False, False)

icon = PhotoImage(file="image/icon.png")
app.iconphoto(True, icon)

#váriaveis globais
input_medidas = StringVar(value="None")
input_valores = StringVar(value="")

#FRAME DO MENU DE ESCOLHA
frame_menu = Frame(app, bg=bg1, width=500, height=250)
frame_menu.pack()
frame_menu_resultado = Frame(app, width=500, height=200, bg=bg1)
frame_menu_resultado.pack()

Title_label = Label(
    frame_menu, 
    bg="#121212", 
    font=(txt, 18, "bold"), 
    fg="#f3f3f3", 
    text="Converter"
)
Title_label.place(x=10, y=10)

#Box interativa da medição de Peso
peso_frame = Frame(frame_menu, width=150, height=180, bg="#151515")
peso_frame.place(x=10, y=50)

title_peso = Label(
    peso_frame, 
    font=(txt, 12, "bold"),
    bg=bg2, 
    fg=fontcor, 
    text="Massa", 
    justify="center"
)
title_peso.place(x=50, y=5)

input_mg = Radiobutton(
    peso_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2, 
    text="Centigrama", 
    selectcolor=bg1, 
    variable=input_medidas, 
    value="mg"
)
input_mg.place(x=15, y=45)

input_g = Radiobutton(
    peso_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2,
    text="Grama", 
    selectcolor=bg1, 
    variable=input_medidas, 
    value="g"
)
input_g.place(x=15, y=85)

input_kg = Radiobutton(
    peso_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2,
    text="Quilograma", 
    selectcolor=bg1, 
    variable=input_medidas, 
    value="kg"
)
input_kg.place(x=15, y=125)

#Box interativa da medição de Distância
distancia_frame = Frame(frame_menu, width=150, height=180, bg="#151515")
distancia_frame.place(x=175, y=50)  

title_distancia = Label(
    distancia_frame, 
    font=(txt, 12, "bold"), 
    bg=bg2, 
    fg=fontcor, 
    text="Distância", 
    justify="center"
)
title_distancia.place(x=25, y=5)

input_cm = Radiobutton(
    distancia_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2,
    text="Centímetro",
    selectcolor=bg1, 
    variable=input_medidas,
    value="cm"
)
input_cm.place(x=15, y=45)

input_m = Radiobutton(
    distancia_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2,
    text="Metro", 
    selectcolor=bg1, 
    variable=input_medidas, 
    value="m"
)
input_m.place(x=15, y=85)

input_km = Radiobutton(
    distancia_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2,
    text="Quilômetro",
    selectcolor=bg1, 
    variable=input_medidas,
    value="km"
)
input_km.place(x=15, y=125)

tempo_frame = Frame(width=150, height=180, bg="#151515")
tempo_frame.place(x=340, y=50)

title_tempo = Label(
    tempo_frame,
    font=(txt, 12, "bold"), 
    bg=bg2,
    fg=fontcor, text="Tempo", 
    justify="center"
)
title_tempo.place(x=50, y=5)

input_seg = Radiobutton(
    tempo_frame,
    font=(txt, 10, "bold"),
    fg=fontcor,
    bg=bg2,
    text="Segundos", 
    selectcolor=bg1, 
    variable=input_medidas, 
    value="seg"
)
input_seg.place(x=15, y=45)

input_min = Radiobutton(
    tempo_frame,
    font=(txt, 10, "bold"),
    fg=fontcor,
    bg=bg2,
    text="Minutos", 
    selectcolor=bg1,
    variable=input_medidas, 
    value="min"
)
input_min.place(x=15, y=85)

input_hora = Radiobutton(
    tempo_frame,
    font=(txt, 10, "bold"),
    fg=fontcor,
    bg=bg2,
    text="Horas", 
    selectcolor=bg1,
    variable=input_medidas,
    value="h"
)
input_hora.place(x=15, y=125)

#FRAME DO INPUT DE USUÁRIO
input_frame = Frame(app, width=480, height=140, bg=bg2)
input_frame.place(x=10, y=250)

resultado_label = Frame(app, width=304, height=95, bg="white")
resultado_label.place(x=15, y=290)

result_1 = Label(resultado_label, text="", font=(txt, 10, "bold"),fg="black")
result_1.place(x=10, y=10, )
result_2 = Label(resultado_label, text="", font=(txt, 10, "bold"),fg="black")
result_2.place(x=10, y=30, )

input_campo = Entry(width=30, bg=fontcor, font=(txt, 12, 'bold'), textvariable=input_valores)
input_campo.configure(validate="key", validatecommand=(app.register(numeric_filter), "%S"))
input_campo.place(x=15, y=255)

button = Button(
    text="Converter",
    height=8, 
    width=19, 
    bg="#232323", 
    fg=fontcor,
    command=converter
)
button.place(x=342, y=255)


mainloop()