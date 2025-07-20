x = float(input('Digite a coordenada X: '))
y = float(input('Digite a coordenada Y: '))

if x > 0 and y > 0:
    print("O ponto está no **Primeiro Quadrante**.")
elif x < 0 and y > 0:
    print("O ponto está no **Segundo Quadrante**.")
elif x < 0 and y < 0:
    print("O ponto está no **Terceiro Quadrante**.")
elif x > 0 and y < 0:
    print("O ponto está no **Quarto Quadrante**.")
else:
    print("O ponto está **no eixo ou na origem**.")