def archExist(name): #Verifica se já existe um arquivo ou não;
    try:
        op = open(name, 'rt')
        op.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createarch(name): #Cria um arquivo txt para adicionar as palavras;
    try:
        op = open(name, 'wt+')
        op.close()
    except:
        print('There was an error creating file!')
    else:
        print(f'Archive {name} was created successfully')


def register(arq, name='unknown'): #Registra o nome das palavras correspondentes;
    try:
        op = open(arq, 'at')
    except:
        print('There was an error opening the file!')
    else:
        try:
            op.write(f'{name}\n')
        except:
            print('There was an error to write the data!')
        else:
            print(f'Add a new register {name}')
            op.close()
