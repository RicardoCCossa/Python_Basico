idade = int(input('Qual eh sua idade:\n'))

if idade <= 12:
    print('Criança')
elif idade <= 18:
    print('Adolescente')
else:
    print('Adulto')