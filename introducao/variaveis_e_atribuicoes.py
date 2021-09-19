"""
    A forma padrão para a instrução de atribuição entre variáveis é:
    <variavel> = <valor>
    A declaracao valor que é atribuida em variavel, pode ser um valor booleano,
    algébrico entre outras expressões como uma cadeia de caracteres.
    IMPORTANTE:
    variáveis declaradas e não inicializadas em Python, acarretará na mensagem:
    NameError: name '<variavel>' is not defined.
    <variavel> aqui é qualquer declaracao de variavel sem um valor atribuido.

"""

ano_nascimento = 1980  # instrução de atribuição
ano_atual = 2021
# operação de subtração de duas variáveis
idade = ano_atual - ano_nascimento
print("Idade atual:", idade)

cor = "azul"  # expressões de atribuição do tipo cadeia de caracteres
