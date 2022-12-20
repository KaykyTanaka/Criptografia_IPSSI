from tkinter import Tk
from tkinter.filedialog import askopenfilename

print('Selecione um arquivo para Criptografar/Descriptografar')
Tk().withdraw()
select = askopenfilename()

arquivo = open(select, "r") 
texto = arquivo.read().lower()
arquivo.close() 

chave = int(input('Digite a chave: '))
opcao = input('Para Criptografar digite C e para Descriptografar digite D: ')
alfabeto = 'abcdefghijklmnopqrstuvwxyz' 
novaMsg = ''

for x in texto:
    if x in alfabeto:
        indice = alfabeto.index(x) 
        
        if opcao == 'C':
            novaMsg += alfabeto[(indice + chave) % len(alfabeto)]
            arquivo2 = open("criptografado.txt", "w") 
        
        elif opcao == 'D':
            novaMsg += alfabeto[(indice - chave) % len(alfabeto)]
            arquivo2 = open("descriptografado.txt", "w")
    else:
        novaMsg += x 

arquivo2.write(novaMsg)
arquivo2.close()
print('Finalizado!')

