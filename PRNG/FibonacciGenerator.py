#############################################################
# Fibonacci é a sequência gerada por
# Sn = S(n-1) + S(n-2)
# Generalizando para gerar números aleatórios,
# podemos gerar (com offsets j e k) de forma cíclica
# (com mod m), pela seguinte fórmula
# Sn = S(n-j) ★ S(n-k) (mod m), 0 < j < k
# onde o operador ★ pode ser adição, subtração,
# multiplicação ou XOR binário
# fontes:
    # https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator
    # https://medium.com/asecuritysite-when-bob-met-alice/for-the-love-of-computing-the-lagged-fibonacci-generator-where-nature-meet-random-numbers-f9fb5bd6c237
#############################################################

class FibonacciGenerator:
    # aqui vamos usar uma determinada seed,
    # tal como j e k fixos em 3 e 7, respectivamente
    # os valores podem ser mudados na instanciação
    # para fornecer maior randomicidade
    def __init__(self, seed = 8675319, j = 3, k = 7, sizeBit = 32):
        self.seed = toList(seed)
        self.j = j
        self.k = k
        self.m = 2 ** sizeBit # para fazer números de n tamanho, vamos fazer módulo de 2^quantidade de bits
        self.sizeBit = sizeBit # guardar tamanho de bits que quer fazer o número aleatório

    def next(self):
        num1 = self.seed[self.j - 1] # pega número da posição j-1
        num2 = self.seed[self.k - 1] # pega número da posição k-1

        # usar operador como sendo multiplicação (*)
        numGenerated = (num1*num2) % self.m # faz a conta de fibonacci usando operador * e módulo m
        self.seed.append(numGenerated) # adiciona o número gerado na última posição (para continuar sequência Fib)
        self.seed.pop(0) # remove o primeiro número, para continuar randomicidade

        return numGenerated
    
    # gera números aleatórios até alcançar a quantidade de bits solicitada
    def generateNumOfBits(self):
        while True:
            randomNumber = self.next()
            if (len(bin(randomNumber)[2::])) == self.sizeBit:
                return randomNumber
                break

# função auxiliar para transformar número em lista de números
def toList(number):
    return list(map(int, str(number)))

def main():
    generator = FibonacciGenerator()
    generator.generateNumOfBits()

if __name__ == "__main__":
    main()