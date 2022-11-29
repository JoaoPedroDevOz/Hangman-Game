def archExist(name):
    try:
        op = open(name, 'rt')
        op.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createarch(name):
    try:
        op = open(name, 'wt+')
        op.close()
    except:
        print('There was an error creating file!')
    else:
        print(f'Archive {name} was created successfully')


def register(arq, name='unknown'):
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
            
def keeping(option):
    while option != 'N':
        keeping(option)
        while option not in 'YN':
            keeping(option)
            if option == 'N':
                break
    return option