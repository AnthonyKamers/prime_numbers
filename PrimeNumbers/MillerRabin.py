#############################################################
# Teste de primalidade de Miller-Rabin
# Teste probabilístico em tempo polinomial
# Segundo o wikipedia, o algoritmo (pseudo-código) é o seguinte:
'''
write n as 2r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
WitnessLoop: repeat k times:
    pick a random integer a in the range [2, n − 2]
    x ← a^d mod n
    if x = 1 or x = n − 1 then
        continue WitnessLoop
    repeat r − 1 times:
        x ← x^2 mod n
        if x = n − 1 then
            continue WitnessLoop
    return “composite”
return “probably prime”
'''
# Vamos fazer algumas adaptações, para que fique mais simples e mais "pythônico"
# Fontes:
    # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    # https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
#############################################################

import random # para pegar números aleatórios dentro do "range" de números

# n = valor de teste de primalidade
# k = parâmetro que determina a precisão do teste
def MillerRabin(n, k):
    # se n for <= 3, é fixamente primo
    if n <= 3:
        return True
    
    # qualquer múltiplo de 2 (par), não é primo por definição
    if n % 2 == 0:
        return False
    
    # identificar variáveis auxiliares do algoritmo
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d //= 2

    # continuação do algoritmo
    for _ in range(k):
        a = random.randint(2, n-1)
        x = pow(a, d, n) # x = (a**d) % n # trocado por ser mais eficiente

        if x == 1 or x == n-1:
            continue

        for _ in range(r-1):
            x = pow(x, 2, n) # x = (x**2) % n # trocado por ser mais eficiente

            if x == n-1:
                break
        else:
            return False
    return True

def main():
    k = 4
    for i in range(1, 101):
        print(f'{i} = {MillerRabin(i, k)}')

if __name__ == "__main__":
    main()