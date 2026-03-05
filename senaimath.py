def Pi():
    soma = 0
    for n in range(10000000):
        base = (2 * n)+1

        formula = 1 / base

        if n % 2:
            soma -= formula
        else:
            soma += formula

    pi = 4 * soma
    return pi
    