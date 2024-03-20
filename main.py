def func(): # cria a função
    lista=[] # cria a lista
    while True: # um laço de repetição para que a condição seja aplicada até que a condição seja falsa
        dados = input('adicione seu numerou ou digite sair: ') # input para colher a condição do usuario
        if dados.lower() == 'sair': # laço é aplicado até o usuario escrever sair
            print(lista) # mostra a lista após o usuario sair
            print(max(lista)) # printa o maior numero numero da lista
            break # para o laço assim que a condição seja falsa
        else:
            lista.append(int(dados)) ## cada loop feito o append adiciona o numero que o usuario digitou na lista


func()
