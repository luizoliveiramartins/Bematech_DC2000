import PySimpleGUI as tela

layout=[
    [tela.InputText(),tela.FileBrowse('Procurar',button_color=('white','blue'))],
    [tela.InputText(),tela.FileSaveAs('Salvar',button_color=('black','yellow'))],
    [tela.Output(size=(30,20))],
    [tela.Button('Ok',button_color=('white','green')),tela.Button('Cancel',button_color=('white','red'))]
    ]
window=tela.Window('INVENTÁRIO',layout)
esquerda=[]
direita=[]
lista=[]
resultado=[]
cont=0
while True:
    event,values=window.read()
    if event=='Ok':
        arquivo=open(values[0],'r')
        gravar=open(values[1]+'.txt','w')
        for a in arquivo:
            lista.append(a.strip())
        for l in lista:
            c=l.split(';')
            esquerda.append(c[0])
            direita.append(int(c[1]))
        for e in esquerda:
            pos=direita.index(direita[0])
            while cont<direita[0]:
                resultado.append(e)
                cont=cont+1
            if cont>0:
                cont=0
            del direita[pos]
        for r in resultado:
            gravar.write(str(r))
            gravar.write('\n')
            print(r)
        gravar.close()
        print('------------------------------------------------')
        print('Arquivo Gerado ok')
        print('Total de Arquivos gerados:',len(resultado))
    if event=='Cancel':
        break

window.close()
arquivo.close()
