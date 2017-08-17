# coding: latin-1

from string import join
import string

# programa que criptografa um determinado texto

print ' '

opt = str(raw_input('Você quer criptografar(1) ou descriptografar(2)? '))

alfabetoOrig = string.ascii_lowercase
alfabetoOrig = list(alfabetoOrig)
lista_final = []


texto = str(raw_input('Insira o texto: '))
listaTexto = list(texto)
print ''

if(opt is '1'):
    for i in listaTexto:
        pos = alfabetoOrig.index(i)
        pos += 3
        try:
            lista_final.append(alfabetoOrig[pos])
        except:
            alfabeto_novo = alfabetoOrig + alfabetoOrig
            lista_final.append(alfabeto_novo[pos])

    textFim = join(lista_final, '')
    print ('Texto criptografado %s') % textFim
    print ''

elif(opt is '2'):
    for i in listaTexto:
        pos = alfabetoOrig.index(i)
        pos -= 3
        try:
            lista_final.append(alfabetoOrig[pos])
        except:
            alfabeto_novo = alfabetoOrig + alfabetoOrig
            lista_final.append(alfabeto_novo[pos])

    textFim = join(lista_final, '')
    print ('Texto descriptografado %s') % textFim
    print ''
