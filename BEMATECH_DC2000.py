import copy
import os
caminho = ('c:/inventario')
 
if not os.path.exists(caminho):
    os.makedirs(caminho)


arquivo=open('c:/inventario/Upload_Data.txt','r')
lista=[]
esquerda=[]
direita=[]
resultado=[]
cont=0

for i in arquivo:
    lista.append(i)

lista.pop(0)
for i in lista:
    c=copy.deepcopy(i.split(';'))
    esquerda.append(c[0])
    direita.append(int(c[1]))
    
for i in esquerda:
    pos2=direita.index(direita[0])
    while cont<direita[0]:
        resultado.append(i)
        cont=cont+1
    if cont>0:
        cont=0
    del direita[pos2]

novo=open('c:/inventario/ARQUIVO_INVENTARIO.txt','w')

for i in resultado:
    novo.write(str(i))
    novo.write(str('\n'))
print('Arquivo Gerado com Sucesso')
novo.close()

arquivo.close()
