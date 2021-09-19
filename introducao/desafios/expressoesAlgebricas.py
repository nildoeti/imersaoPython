"""
    Escreva expressões algébricas correspondentes aos seguintes comandos:
    (a) A soma dos 5 primeiros inteiros positivos.
    (b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
    (c) O número de vezes que 73 cabe em 403.
    (d) O resto de quando 403 é dividido por 73.
    (e) 2 à 10 a potência.
    (f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a
        altura de Mark (57 polegadas).
    (g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
"""

# (a) A soma dos 5 primeiros inteiros positivos.
print(5 + 6 + 6 + 7 + 8)
# (b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
sara = 23
mark = 19
fatima = 31

idade_media = (sara + mark + fatima) / 3

print("Idade média é: ", idade_media)

# (c) O número de vezes que 73 cabe em 403.
print(403 // 73)

# (d) O resto de quando 403 é dividido por 73.
print(404 % 73)

# 2 à 10 a potência.
print(2 ** 10)

# (f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a
#     altura de Mark (57 polegadas).

print(abs(54 - 57))

# (g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
print(min(43.99, 29.95, 31.59))
