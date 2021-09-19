"""
    Boolean são expressões que tem como resultado um valor
    verdadeiro(true) ou falso(false)
"""

print(2 < 3)  # true
print(3 < 2)  # false
print(4 <= 4)  # true
print(4 >= 4)  # true
print((4 < 4))  # false
print((3 != 4))  # true

# operadores algébricos + e - tem precedência sobre os operadores de comparação
print(5 - 1 > 2 + 1)  # false

# igualdade entre dois valores algébricos
print(3 + 5 == 4 + 4)  # true
print(3 + 5 == 4 - 4)  # false
print(0 - 1 == 5)  # false
