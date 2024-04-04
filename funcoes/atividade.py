# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

resultado = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    
    for  i , opcao in enumerate(pergunta['Opções']):
        print(f'{i})',opcao)
        print()
    
    escolha=input('Escolha uma opção: ')

    if escolha == pergunta['Resposta']:
        print('certa resposta!!')
        resultado += 1
    else:
        print('errado sua mula')
    #for resposta in pergunta['Resposta']:
print(resultado,': quantidade de respostas certas!!')
    

        
#   escolha= None
#    acertou = False
#    2.5

#    if escolha.isdigt():
#        escolha = int(escolha)
#    
#    if escolha is not None:
#        print('tal') '''
        
    
    

        