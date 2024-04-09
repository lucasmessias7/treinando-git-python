from dados import dados

def ctb():
    for j in range(0,1):
        if idade < 3 and sexo == 'mulher':
            basal = (58.317 * peso) - 31.1
            print(f'seu basal é: {basal:.2f}')
        elif idade < 3 and sexo == 'homem':
            basal = (59.512 * peso) - 30.4
            print(f'seu basal é: {basal:.2f}')

        if idade < 10 and sexo == 'mulher' : 
            basal = (20,315 * peso) + 485.9
            print(f'seu basal é: {basal:.2f}')
        elif idade < 10 and sexo == 'homem':
            basal = (22.706 * peso) + 504.3
            print(f'seu basal é: {basal:.2f}')

        if idade < 18 and sexo == 'mulher':
            basal = (13,384 * peso) + 692.6
            print(f'seu basal : {basal:.2f}')
        elif idade < 18 and sexo == 'homem':
            basal = (17.686 * peso) + 658.2
            print(f'seu basal é: {basal:.2f}')

        if idade < 30 and sexo == 'mulher': 
            basal = (14.818 * peso) + 486.6
            print(f'seu basal é: {basal:.2f}')
        elif idade < 30 and sexo == 'homem':
            basal = (15.057 * peso) + 692.2
            print(f'seu basal é: {basal:.2f}')

        if idade < 60 and sexo == 'mulher':
            basal = (8.126 * peso  )+ 845.6
            print(f'seu basal é: {basal:.2f}')
        elif idade < 60 and sexo == 'home':
            basal = (11.472 * peso) + 873.1
            print(f'seu basal é: {basal:.2f}')

        if idade > 60 and sexo == 'mulher':
            basal = (9.082 * peso  )+ 658.5
            print(f'seu basal é: {basal:.2f}')
        elif idade > 60 and sexo == 'homem' :
            basal = (11.711 * peso) + 587.7
            print(f'seu basal é: {basal:.2f}')