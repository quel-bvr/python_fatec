# import random 
# 
# 
# 
# # código digitado pelo usuário 
# entrada_do_usuario = 7
# numero_que_deve_ser_advinhado = 7
# 
# if entrada_do_usuario == numero_que_deve_ser_advinhado:
#     print("deu sorte hein")
# else:    
#     print( "iiii errouuuu")

import random

#programa com numero aleatório 
entrada_do_usuario = input("digite um valor aqui: ")
numero_que_deve_ser_advinhado = random.randint(1, 10)

if entrada_do_usuario == numero_que_deve_ser_advinhado:
  print("deu sorte hein")
else:
    print( "iiii errouuuu")