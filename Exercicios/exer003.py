nome = 'Ricardo'.capitalize()
senha = 1234

nome_digitado = input('Digite o nome:\n').capitalize()
senha1 = int(input('Digite a senha:\n'))

if nome == nome_digitado and senha == senha1:
    print('Nome e senha iguais')
else:
    print('Nome ou senha incorrectos')