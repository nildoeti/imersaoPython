# expressões com operadores algébrico
soma = 3 + 7
print(soma)

subtracao = 5 - 3
print(subtracao)

multiplicacao = 3 * 5
print(multiplicacao)

# python sempre retornar um número decimal' com divisão de números inteiros
divisao = 4 / 2
print(divisao)

restoDivisao = 5 % 2
print(restoDivisao)

# regras de precedências entre operadores
multiplosOperadores1 = 2 * 3 + 1  # multiplica e soma o resultado
print(multiplosOperadores1)

regrasPrecedencia2 = (2 * 3) + 1  # primeiro a multiplicação seguida da adição
print(regrasPrecedencia2)

regrasPrecedencia3 = 4.321 / 3 + 10  # primeiro a divisao seguida da adição
print(regrasPrecedencia3)

# potencia de um número
potenciaNumero = 2 ** 4
print(potenciaNumero)

# obtendo dois quociênte e resto inteiros
quocienteInteiro1 = 14 // 3
print(quocienteInteiro1)

quocienteInteiro2 = 14 % 3  # resto da divisao de 14 por 3
print(quocienteInteiro2)

# funções como expressões matemáticas em Python

# função abs() de Python retorna o valor absoluto de um números
valorAbsoluto1 = abs(-4)
valorAbsoluto2 = abs(-14.7)

print(valorAbsoluto1)
print(valorAbsoluto2)


# funções min() e max(), retorna o menor e maior valor entre duas expressões
print(min(5, 9, -1))  # menor valor entre três números
print(max(99, -5, 78))  # maior valor entre três números
