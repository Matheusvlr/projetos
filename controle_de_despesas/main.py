from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
# importando barra de progresso do Tkinter
from tkinter.ttk import Progressbar
# importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

################# cores ###############
cor0 = "#2e2d2b"  
cor1 = "#feffff"  
cor2 = "#4fa882"  
cor3 = "#38576b"  
cor4 = "#403d3d"   
cor5 = "#e06636"   
cor6 = "#038cfc"   
cor7 = "#3fbfb9"   
cor8 = "#263238"   
cor9 = "#e9edf5"   

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

# criação da janela
janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use('clam')

# criação dos frames para divisão da tela
############################## frame de cima ##############################
frame_cima = Frame(janela, width=1043, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, column=0)

############################## frame do meio ##############################
frame_meio = Frame(janela, width=1043, height=361, bg=cor1, pady=20, relief='raised')
frame_meio.grid(row=1, column=0, pady= 1, padx= 0, sticky=NSEW)

############################## frame de baixo ##############################
frame_baixo = Frame(janela, width=1043, height=300, bg=cor1, relief='flat')
frame_baixo.grid(row=2, column=0, pady= 0, padx= 10, sticky=NSEW)

# desenvolvendo o frame de cima

# acesso a imagem
app_img = Image.open('controle_de_despesas/logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text=' CONTROLE DE ORÇAMENTO', width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)

# porcentagem
def porcentagem():
    lab_nome = Label(frame_meio, text='Porcentagem de Gastos', height=1, anchor=NW, font=('verdana 12'), bg=cor1, fg=cor4)
    lab_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('black.Horizontal.TProgressbar', background='#daed6b')
    style.configure('TProgressbar', thickness=25)
    barra = Progressbar(frame_meio, length=180, style='black.Horizontal.TProgressbar')

    barra = Progressbar(frame_meio, length=180)
    barra.place(x=10, y=35)
    barra['value'] = 50

    valor = 50

    lab_porcentagem = Label(frame_meio, text=f'{valor:,.2f}%', height=1, anchor=NW, font=('verdana 12'), bg=cor1, fg=cor4)
    lab_porcentagem.place(x=200, y=35)


porcentagem()
janela.mainloop() 