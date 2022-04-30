from posixpath import split
from time import sleep
from tkinter import Menu


opcoes = ['chá', 'chocolate quente', 'espresso', 'caputino']
 
for posicao, opcoes in enumerate(opcoes):
    print (f"{posicao +1} - {opcoes}")
 
pedido = input ("selecione uma das opções acima ")
 

#lendo banco de dados 
def ler_banco():
    """Essa funcao le um banco de dados"""
    with open("estoque.csv", "r") as file:
        dados_do_banco = file.read ()

        dados_do_estoque = dados_do_banco.split("\n")
        menu = dados_do_estoque[0],split(",")
        quantidade_no_estoque = dados_do_estoque[1].split(",")
        return Menu, quantidade_no_estoque
           
itens_menu = ler_banco()[0]
estoque_menu = ler_banco()[1]   
    
for posicao, item in enumerate (itens_menu):
    print(f"[{posicao + 1}] - {item}")
pedido = input (">>> ")
        
tamanho_menu = len(itens_menu)

if pedido > tamanho_menu or pedido < 1:
    print ("Opção inválida")
    
    pedido = pedido - 1
    estoque_menu[pedido] = int(estoque_menu[pedido] - 1)
     print (estoque_menu)
     
     with open (estoque)