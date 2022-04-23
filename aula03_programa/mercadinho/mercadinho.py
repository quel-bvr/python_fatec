#author: raquel bitar
#version: 1.0.1
#date: abr/09/2022
#descripition: este programa para cadastrar usuarios
#name: mercadinho fatec

from hashlib import sha256
from itertools import count
import sys
from time import sleep

mensagem = "Olá seja bem-vindo ao Mercadinho Fatec"

for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
    sleep(0.1)
print() 
    
opcoes_de_login = [" sing in", "sing up", "fale conosco"]

count = 1
for opcao in opcoes_de_login:
    print(f"[{count}] - {opcao}")
    count +=1 # count = count + 1

opcao_digitada = input ("qual opcao vc deseja? ")


with open ("./db.csv") as arquivo:
     print (arquivop.read())