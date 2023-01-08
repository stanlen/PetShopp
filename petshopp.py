

from tkinter import *
from functions import *
import tkinter as janela


class Petshopp:
  
  janela = Tk()
  janela.title("PETSHOPP")
  janela.geometry('1070x600+150+1')



  # FUNÇÃO DO BOTÃO INICIAL PET
  def botao_click1():
    pass

  # FUNÇÃO DO BOTÃO INICIAL CLIENTES
  def botao_click2():
    pass


  #FUNÇÃO DO BOTÃO ADOÇÃO
  def botao_click3():
    pass
    
  def botao_click4():
    pass

  #código princial
  botao_1 = Button(janela, text = "PETS", padx = 45, pady = 45, borderwidth = 5, background='#4169E1', command = lambda: janela.botao_click1())
  botao_2 = Button(janela, text = "CLIENTES", padx = 45, pady = 45, borderwidth = 5,background='#4169E1', command = lambda: janela.botao_click2())
  botao_3 = Button(janela, text = "ADOÇOES", padx = 45, pady = 45, borderwidth = 5, background='#4169E1',command = lambda: janela.botao_click3())
  botao_4 = Button(janela, text = "RELATÓRIOS", padx = 45, pady = 45, borderwidth = 5, background='#4169E1',command = lambda: janela.botao_click4())
  botao_5 = Button(janela, text = "SAIR", padx = 45, pady = 45, borderwidth = 5,background='#4169E1', command = lambda: exit())

  botao_1.grid(row = 0, column = 0,columnspan=1, ipadx = 45)
  botao_2.grid(row = 1, column = 0,columnspan=1, ipadx = 32)
  botao_3.grid(row = 2, column = 0,columnspan=1, ipadx = 31)
  botao_4.grid(row = 3, column = 0,columnspan=1, ipadx = 25)
  botao_5.grid(row = 4, column = 0,columnspan=1, ipadx = 45)


Petshopp()
