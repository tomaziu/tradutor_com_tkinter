from tkinter import Tk, ttk, Text, Button
from translate import Translator
from ttkbootstrap import Style

# Tk default
# janela = Tk()

# janela = ThemedTk(theme='equilux')

estilo = Style(theme='darkly')
janela = estilo.master

janela.title('Tradutor TOP DMAIZE')

frame_geral = ttk.Frame()
frame_geral.pack()

def traduzir(evento='Arial'):
    
    translator = Translator(
        from_lang=combo_entrada.get(),
        to_lang=combo_saida.get()
)

    texto = entrada.get('1.0', 'end')

    traducao = translator.translate(texto)
    
    saida.delete('1.0')
    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', traducao)
    saida.configure(state='disabled')


values = ['pt', 'en', 'es']

frame_entrada = ttk.Frame(frame_geral)
label_entrada = ttk.Label(
    frame_entrada,
    text='Entrada',
    font=('Arial', 10)
)
combo_entrada = ttk.Combobox(
    frame_entrada,
    values=values,
    font=('Arial', 10)
)
entrada = Text(
    frame_geral,
    padx=5,
    pady=5,
    height=10,
    width=50,
    font=('Arial', 15)
)

label_entrada.grid(
    row = 0,
    column = 0,
    padx=5,
    pady=5
)
combo_entrada.grid(
    row = 0,
    column = 1,
    padx=5,
    pady=5
)

combo_entrada.set('pt')
frame_entrada.pack()

entrada.pack(
    padx=10,
    pady=5,
    fill=('both'),
    expand='yes',
)

# Saída ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frame_saida = ttk.Frame(frame_geral)
label_saida = ttk.Label(
    frame_saida,
    text='Saida',
    font=('Arial', 10)
)
combo_saida = ttk.Combobox(
    frame_saida,
    values=values,
    font=('Arial', 10)
)
saida = Text(
    frame_geral,
    padx=5,
    pady=5,
    height=10,
    width=50,
    font=('Arial', 15),
    state='disabled'
)

label_saida.grid(
    row = 0,
    column = 0,
    padx=5,
    pady=5
)
combo_saida.grid(
    row = 0,
    column = 1,
    padx=5,
    pady=5,
)

combo_saida.set('en')
frame_saida.pack()

saida.pack(
    padx=10,
    pady=5,
    fill=('both'),
    expand='yes'
)

botao = ttk.Button(
    frame_geral,
    text='Traduzir',
    # font=('ArialBold', 15),
    command=traduzir
)
botao.pack(
    fill='both',
    expand='yes',
    padx=5,
    pady=5
)

janela.bind('<Return>', traduzir)

janela.mainloop()