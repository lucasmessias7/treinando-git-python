def calc_imc():
    peso =float(input('digite seu peso: '))
    altura = float(input('digite sua altura: '))
    for i in range(0,1):
        imc =peso / (altura * altura)
        if imc < 18.5:
            print(f'seu imc é: {imc} ,Só a capa do batman')
        elif imc < 24.9:
            print(f'seu imc é: {imc} tá frango, mas está bom.')
        elif imc < 29.9:
            print(f'seu imc é: {imc} está virando uma rolhazinha de poço')
        elif imc < 39.9:
            print(f'seu imc é: {imc} calma o chupeta de baleia')
        else:
            print(f'seu imc é: {imc} Seu peso está desequilibrando o planeta terra')
        

CalculadoraImc = calc_imc()