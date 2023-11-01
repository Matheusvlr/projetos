from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

# cores
cor1 = "#0a0a0a"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.configure(bg=cor2)

# divisão da tela em dois frames
frame_cima = Frame(janela, width=295, height=50, bg=cor2, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Frame cima
img = Image.open('C:\\Users\\Matheus\\Documents\\projetos\\gerador-de-senhas\\img\\gerador.png')
img = img.resize((55, 55), Image.BICUBIC)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS',width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 13 bold'),bg=cor2, fg=cor1)
app_nome.place(x=45, y=13)

app_linha = Label(frame_cima, text='',width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1 bold'),bg=cor2, fg=cor1)
app_linha.place(x=0, y=35)


estilo = ttk.Style(janela)
estilo.theme_use('clam')

janela.mainloop()