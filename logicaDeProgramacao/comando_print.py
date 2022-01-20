'''
    Print é uma função de Python para exibir mensagens em sua saida padrão.
'''
print('')  # print sem argumento
print('Um simples texto.')  # print com um argumento do tipo strings
print('um', 'dois', 'três')  # print com varios agumentos do tipo strings

# print com sequencias de strings e a função separator sep
print('segunda', 'feira', sep='-')


# print com sequencias de strings e as funções sep e end
print('Terça', 'feira', sep='-', end=' é ')
print('feriado', sep='', end='')


# uso das funções sep e end com print para exibir o número de CPF
print('\n')
print('845', '176', '070', sep='.', end='-')
print('18')
