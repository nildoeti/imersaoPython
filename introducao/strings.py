"""
    Strings são usados assim como na maioria das linguagens de programação,
    são usadas para a manipulação de textos.

    operador <> para comparação de STRING, tem como base a ordem do dicionário

    operador + concatena expressões de strings como um único valor

    operador * não multiplica cadeia de caracteres mas cadeia de caracteres por
    um valor inteiro

    DOCUMENTACÃO
    use help(str), para maiores informações sobre Strings em Python
    x in s # verifica se x está em s
    x in y # verdade para x em t
    x not in y # verdade para x em y
    x + y # concatena x em y
    x*a,a*x # n cópias de x em a
    x + y # concatena x em y
    x[y] # x no índice de y
    len(x) # comprimento de x
    """
cidadeFavorita = "Gramados"  # expressão contendo somente strings

# operadores sobre strings
print(cidadeFavorita == "Gramados")  # True
print(cidadeFavorita == "São Paulo")  # False
print(cidadeFavorita != "Campo Grande")  # True

# comparação de string
print("a" < "b")  # true
print("a" > "b")  # false
print(cidadeFavorita < str(4))  # False

print("no" + "me")  # uso do operador +
print("a" * 5)  # caractere 'a' multiplicado por 5

# expressão in, compara uma se um determinado valor consta em uma variável
print("a" in "a")
print(cidadeFavorita in "são paulo")  # False
print(len("nome"))  # retorna o total de caracteres
