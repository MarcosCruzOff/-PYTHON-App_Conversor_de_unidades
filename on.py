import tkinter as tk
from tkinter import ttk

# Função que formata um valor float com duas casas decimais e vírgulas a cada três dígitos inteiros
def format_value(value):
    return "{:,.2f}".format(value)

# Função que atualiza o valor do label formatado
def update_formatted_label():
    value = float(numeric_entry.get() or 0)
    formatted_label_textvar.set(format_value(value))

# Função que filtra a entrada do usuário para permitir apenas números e ponto decimal
def numeric_filter(value):
    if value.isdigit() or value == "" or value == ".":
        if numeric_entry.index(tk.INSERT) == 0 and value == ".":
            numeric_entry.insert(tk.INSERT, "0.")
            return False
        elif "." in numeric_entry.get() and value == ".":
            return False
        elif value == "":
            return True
        elif len(numeric_entry.get().split(".")[0]) < 3 or numeric_entry.index(tk.INSERT) > len(numeric_entry.get()) - 3:
            return True
    return False

# Criar a janela principal
root = tk.Tk()
root.title("Numeric Entry")

# Criar um objeto Entry que permita apenas números
numeric_entry = tk.Entry(root)
numeric_entry.configure(validate="key", validatecommand=(root.register(numeric_filter), "%S"))
numeric_entry.pack(pady=10)

# Criar um objeto Label que exibe o valor formatado
formatted_label_textvar = tk.StringVar(value="0.00")
formatted_label = ttk.Label(root, text="Valor formatado: ", textvariable=formatted_label_textvar)
formatted_label.pack()

# Configurar o evento de mudança no objeto Entry
numeric_entry.bind("<KeyRelease>", lambda event: update_formatted_label())

# Iniciar o loop principal do aplicativo
root.mainloop()
