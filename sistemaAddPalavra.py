from sistemaAddPalavras import  *

arq = 'Palavras.txt'
ask = ''

if archExist(arq):
    print()
else:
    createarch(arq)



while ask != "N":
    register(arq, str(input("Palavra: ")))
    ask = str(input('Do you want to continue? [YN] ')).upper()
    while ask not in 'YN':
        ask = str(input('Do you want to continue? [YN] ')).upper()
        continue
    if ask == 'N':
        break

