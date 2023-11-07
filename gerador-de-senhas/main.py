from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import string
import random
from tkinter import messagebox

# cores
cor1 = "#0a0a0a"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#f50505"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

janela = Tk()
janela.title('')
janela.geometry('295x360')
janela.configure(bg=cor2)


estilo = ttk.Style(janela)
estilo.theme_use('clam')

# divisão da tela em dois frames
frame_cima = Frame(janela, width=295, height=50, bg=cor2, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor2, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# frame cima
img = Image.open('gerador-de-senhas/gerador.png')
img = img.resize((55, 55), Image.BICUBIC)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS',width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 13 bold'),bg=cor2, fg=cor1)
app_nome.place(x=45, y=13)

app_linha = Label(frame_cima, text='',width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1 bold'),bg=cor6, fg=cor1)
app_linha.place(x=0, y=45)

# função para gerar senha
def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = ':@#*{}[]()_/,-'

    global combinar

    # condição para MAIÚSCULA

    if estado_1.get() == alfabeto_maior:
        combinar = alfabeto_maior
    else:
        pass

    # condção para minúscula
    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass

     # condção para numeros
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass
     # condção para símbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('sucesso', 'A senha foi copiada com sucesso.')

    # botão para copiar senha
    botao_copiar_senha = Button(frame_baixo, command=copiar_senha, text='Copiar',width=7, height=2, relief='raised',overrelief='solid', anchor='center', font=('Ivy 9 bold'),bg=cor2, fg=cor1)
    botao_copiar_senha.grid(row=0, column=2, sticky=NW, padx=5, pady=9, columnspan=1)

# frame de baixo

app_senha = Label(frame_baixo, text='- - - - -', width=25, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 10 bold'),bg=cor2, fg=cor1)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='Número de caracteres na senha', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'),bg=cor2, fg=cor1)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_= 0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = ':@#*{}[]()_/,-'

frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor2, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# letras maiúsculas
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior, offvalue='off', offrelief='flat', bg=cor2)
check_1.grid(row=0, column=0, sticky=NSEW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras maiúsculas (ABC)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'),bg=cor2, fg=cor1)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# letras minúsculas
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_menor, offvalue='off', offrelief='flat', bg=cor2)
check_2.grid(row=1, column=0, sticky=NSEW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras minúsculas (abc)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'),bg=cor2, fg=cor1)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# números
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', offrelief='flat', bg=cor2)
check_3.grid(row=2, column=0, sticky=NSEW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Números (123)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'),bg=cor2, fg=cor1)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

# símbolos
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', offrelief='flat', bg=cor2)
check_4.grid(row=3, column=0, sticky=NSEW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Símbolos (#@*)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'),bg=cor2, fg=cor1)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

# botão gerador de senha
botao_gerador_senha = Button(frame_caracteres, command=criar_senha, text='Gerar Senha',width=34, height=1, relief='flat',overrelief='solid', anchor='center', font=('Ivy 10 bold'),bg=cor6, fg=cor2)
botao_gerador_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=11, columnspan=5)

janela.mainloop()


