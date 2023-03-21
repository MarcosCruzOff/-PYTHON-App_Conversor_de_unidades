from tkinter import *
from tkinter import messagebox

#cores
bg1 = "#121212"
bg2 = "#151515"
button_color = "#232323"
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
input_units = StringVar(value="None")
input_values = StringVar(value="")

#Funções do app
def check_fields():
    if input_units.get() == "None":
        messagebox.showwarning("Aviso","Faça sua escolha primeiro")
    elif input_values.get() == "":
        messagebox.showwarning("Aviso","Insira algum valor primeiro")
    else : 
       return True

def convert():
    if check_fields() == True:
        value = int(input_values.get())
        
        #Unidades de peso
        if input_units.get() == "mg":            
            result_1 = str(format_value(value / 1000)) + "g"            
            result_2 = str(format_value(value / 1000000)) + "kg"             
            list_result = [result_1, result_2]
            showresult["text"] = "\n".join(list_result)
            
        elif input_units.get() == "g":
            result_1 = str(format_value(value * 1000)) + "mg"           
            result_2 = str(format_value(value / 1000 )) + "kg"
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)
                                  
        elif input_units.get() == "kg":            
            result_1 = str(format_value(value * 1000000 )) + "mg"          
            result_2 = str(format_value(value * 1000 )) + "g"   
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)            
            
        #Unidades de distância
        elif input_units.get() == "cm":
            result_1 = str(format_value(value / 100)) + "m"        
            result_2 = str(format_value(value / 100000)) + "km"
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)         
            
        elif input_units.get() == "m":            
            result_1 = str(format_value(value * 100 ))  + "cm"       
            result_2 = str(format_value(value / 1000 ))  + "km"        
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)     
        
        elif input_units.get() == "km":            
            result_1 = str(format_value(value * 100000))  + "cm"         
            result_2 = str(format_value(value * 1000))  + "m"          
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)     
            
        #Unidades de tempo
        elif input_units.get() == "seg":
            result_1 = str(format_value(value * 60 ))  + "min"        
            result_2 = str(format_value(value / 3600 ))  + (" hora" if (value / 3600) < 2 else " horas")      
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)     
            
        elif input_units.get() == "min":            
            result_1 = str(format_value(value * 60)) + "seg"          
            result_2 = str(format_value(value / 60 ))  + (" hora" if (value / 60)  < 2 else " horas")      
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)     
        
        elif input_units.get() == "h":            
            result_1 = str(format_value(value * 3600)) + "seg"          
            result_2 = str(format_value(value * 60))   + "min"         
            showresult["text"] = format_value(result_1) + "seg"
            list_result = [result_1, result_2]         
            showresult["text"] =  "\n".join(list_result)     
        
        else:
            messagebox.showerror("Fudeo","Teu Pc vai explodir")

# Função que filtra a entrada do usuário para permitir apenas números e ponto decimal
def numeric_filter(value):
    if value.isdigit() or value == "" or value == ".":
        if input_field.index(INSERT) == 0 and value == ".":
            input_field.insert(INSERT, "0.")
            return False
        elif "." in input_field.get() and value == ".":
            return False
        elif value == "":
            return True
        elif len(input_field.get().split(".")[0]) < 3 or input_field.index(INSERT) > len(input_field.get()) - 3:
            return True
    return False

# Função que formata um valor float com duas casas decimais e vírgulas a cada três dígitos inteiros
def format_value(value):
    return "{:,.2f}".format(value).replace(",",".")

#FRAME DO MENU DE ESCOLHA
frame_menu = Frame(app, bg=bg1, width=500, height=250)
frame_menu.pack()
frame_menu_resultado = Frame(app, width=500, height=200, bg=bg1)
frame_menu_resultado.pack()

Title_label = Label(
    frame_menu, 
    bg=bg1, 
    font=(txt, 18, "bold"), 
    fg=fontcor, 
    text="Converter"
)
Title_label.place(x=10, y=10)

#Box interativa da medição de Peso
weight_frame = Frame(frame_menu, width=150, height=180, bg=bg2)
weight_frame.place(x=10, y=50)

title_weight = Label(
    weight_frame, 
    font=(txt, 12, "bold"),
    bg=bg2, 
    fg=fontcor, 
    text="Massa", 
    justify="center"
)
title_weight.place(x=50, y=5)

input_mg = Radiobutton(
    weight_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2, 
    text="Centigrama", 
    selectcolor=bg1, 
    variable=input_units, 
    value="mg"
)
input_mg.place(x=15, y=45)

input_g = Radiobutton(
    weight_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2,
    text="Grama", 
    selectcolor=bg1, 
    variable=input_units, 
    value="g"
)
input_g.place(x=15, y=85)

input_kg = Radiobutton(
    weight_frame, 
    font=(txt, 10, "bold"), 
    fg=fontcor, 
    bg=bg2,
    text="Quilograma", 
    selectcolor=bg1, 
    variable=input_units, 
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
    variable=input_units,
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
    variable=input_units, 
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
    variable=input_units,
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
    variable=input_units, 
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
    variable=input_units, 
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
    variable=input_units,
    value="h"
)
input_hora.place(x=15, y=125)

#FRAME DO INPUT DE USUÁRIO
input_frame = Frame(app, width=480, height=140, bg=bg2)
input_frame.place(x=10, y=250)

input_field = Entry(width=30, bg=fontcor, font=(txt, 12, 'bold'), textvariable=input_values)
input_field.configure(validate="key", validatecommand=(app.register(numeric_filter), "%S"))
input_field.place(x=15, y=255)

resulted_label = Frame(app, width=304, height=95, bg="white")
resulted_label.place(x=15, y=290)

showresult = Label(resulted_label, text="", font=(txt, 12, "bold"), bg="white", fg="black", justify="left")
showresult.place(x=15, y=10)

button = Button(
    text="Converter",
    height=8, 
    width=19, 
    bg=button_color, 
    fg=fontcor,
    command=convert
)
button.place(x=342, y=255)

mainloop()