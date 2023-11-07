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

############################## frame de cima ##############################
frame_cima = Frame(janela, width=1043, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, column=0)

############################## frame do meio ##############################
frame_meio = Frame(janela, width=1043, height=361, bg=cor1, pady=20, relief='raised')
frame_meio.grid(row=1, column=0, pady= 1, padx= 0, sticky=NSEW)

############################## frame de baixo ##############################
frame_baixo = Frame(janela, width=1043, height=300, bg=cor1, relief='flat')
frame_baixo.grid(row=2, column=0, pady= 0, padx= 10, sticky=NSEW)


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

# função para gráfico de barra
def grafico_barra():
    lista_categorias =  ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6236]

    # fazer figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    # create a list to collect the plt.patches data

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=10, y=70)


# função de resumo total
def resumo():
    valor = [500, 600, 420]

    l_linha = Label(frame_meio, text='', width=220, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=52)
    l_sumario = Label(frame_meio, text='Total da Renda Mensal      '.upper(), anchor=NW, font=('Verdana 11'), bg=cor1, fg='#83a9e6')
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frame_meio, text=f'R${valor[0]:,.2f}', anchor=NW, font=('Arial 17'), bg=cor1, fg='#545454')
    l_sumario.place(x=309, y=70)

    l_linha = Label(frame_meio, text='', width=225, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=132)
    l_sumario = Label(frame_meio, text='Total de Despesas Mensais '.upper(), anchor=NW, font=('Verdana 11'), bg=cor1, fg='#83a9e6')
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frame_meio, text=f'R${valor[1]:,.2f}', anchor=NW, font=('Arial 17'), bg=cor1, fg='#545454')
    l_sumario.place(x=309, y=150)

    l_linha = Label(frame_meio, text='', width=220, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=207)
    l_sumario = Label(frame_meio, text='Total de Saldo Mensal     '.upper(), anchor=NW, font=('Verdana 11'), bg=cor1, fg='#83a9e6')
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frame_meio, text=f'R${valor[2]:,.2f}', anchor=NW, font=('Arial 17'), bg=cor1, fg='#545454')
    l_sumario.place(x=309, y=220)

# função gráfico pie
def grafico_pie():
    frame_gra_pie = Frame(frame_meio, width=580, height=250, bg=cor2)
    frame_gra_pie.place(x=415, y=5)

############################## frame gráfico ##############################
frame_gra_pie = Frame(frame_meio, width=500, height=250, bg=cor2)
frame_gra_pie.place(x=415, y=5)

# função grafico pie
def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)



porcentagem()
grafico_barra()
resumo()
grafico_pie()

# criação dos frames de dentro do frame baixo
frame_renda = Frame(frame_baixo, width=300, height=250, bg=cor1)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frame_baixo, width=220, height=250, bg=cor1)
frame_operacoes.grid(row=0, column=1, padx=5)

frame_configuracao = Frame(frame_baixo, width=220, height=250, bg=cor1)
frame_configuracao.grid(row=0, column=2, padx=5)

# tabela de renda mensal
app_tabela = Label(frame_meio, text='Tabela de Receitas e Despesas', anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
app_tabela.place(x=5, y=309)

# função para mostrar a renda
def mostrar_renda():
     #criando uma treeview com barras de rolagem duplas
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
     # ajusta a largura da coluna de acordo com a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostrar_renda()





janela.mainloop() 