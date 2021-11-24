#############################################################
# Teste de primalidade de Solovay-Stressen
# Teste probabilístico de ordem O(k * log3 n)
# Segundo o wikipedia, o algoritmo (pseudo-código) é o seguinte:
'''
repeat k times:
    choose a randomly in the range [2,n − 1]
    x = legendre(a, n)
    if x = 0 or a^((n-1)/2) != x
        return composite
return probably prime
'''
# Vamos fazer algumas adaptações, para que fique mais simples e mais "pythônico"
# Fontes:
    # https://en.wikipedia.org/wiki/Solovay%E2%80%93Strassen_primality_test
    # https://www.geeksforgeeks.org/primality-test-set-4-solovay-strassen/
#############################################################

import random

# função auxiliar usada para resolver primalidade
# de Euler, no algoritmo de Solovay-Stressen,
# usando Legendre
def legendre(a, n):
    if a == 0 or a == 1:
        return a

    if a % 2 == 0:
        r = legendre(a//2, n)
        
        if pow(n, 2) - 1 & 8 != 0:
            r *= -1
    else:
        r = legendre(n%a, a)
        if (a-1) * (n-1) & 4 != 0:
            r *= -1
    
    return r

# n = valor de teste de primalidade
# k = parâmetro que determina a precisão do teste
def SolovayStressen(n, k):
    # se n for <= 3, é fixamente primo
    if n <= 3:
        return True

    # qualquer múltiplo de 2 (par), não é primo por definição
    if n % 2 == 0:
        return False

    # continuação do algoritmo
    for _ in range(k):
        a = random.randint(2, n-1)
        x = legendre(a, n)
        aux = (n-1)//2

        if x == 0 or (pow(a, aux) % n) != (x % n):
            return False

    return True

def main():
    k = 4
    for i in range(1, 101):
        print(f'{i} = {SolovayStressen(i, k)}')

if __name__ == "__main__":
    main()