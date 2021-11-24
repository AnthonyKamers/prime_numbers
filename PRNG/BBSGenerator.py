#############################################################
# Fazer um PRNG usando o altoritmo de Blum Blum Shub (BBS)
# Proposto em 1968, usa o a função de um-caminho de Michael Rabin
# da função de primalidade Miller-Rabin. A fórmula do algoritmo é:
# X(n+1) = X(n)^2 mod M
    # X(0) = seed (co-primo de M)
    # M = p * q
        # p e q são primos congruentes a 3 (mod 4)
# fontes:
    # https://en.wikipedia.org/wiki/Blum_Blum_Shub
    # https://asecuritysite.com/encryption/blum
    # https://github.com/VSpike/BBS/tree/9be96e30acd072db61ed2c05ba4c1a5044ea554e
#############################################################

from .RandomGenerator import generate_prime_number

class BBSGenerator:
    def __init__(self, seed = 3, sizeBit = 2048, sizeBit1 = None):
        # como precisamos de 2 números primos para serem multiplicados
        # entre si (pelo algoritmo) e precisamos também que seja gerado um número
        # com determinado número de bits, vamos gerar, com a ajuda
        # do código retirado de https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb,
        # somente para ter parâmetros necessários para o funcionamento completo do algoritmo.
        # Dessa maneira, quando forem multiplicados,
        # com certeza gerarão um número maior que sizeBit bits
        self.p = generate_prime_number(sizeBit1 if sizeBit1 is not None else sizeBit)
        self.q = generate_prime_number(sizeBit1 if sizeBit1 is not None else sizeBit)
        self.m = self.p * self.q # multiplicação de p por q
        self.seed = seed
        self.sizeBit = sizeBit

    def next(self):
        self.seed = (self.seed ** 2) % self.m
        return self.seed

    # gera números aleatórios até alcançar a quantidade de bits solicitada
    def generateNumOfBits(self):
        while True:
            # para forçar ser do tamanho de bits que queremos,
            # vamos fazer o número gerado mod 2^self.sizeBit
            randomNumber = self.next() % (2 ** self.sizeBit)

            if (len(bin(randomNumber)[2::])) == self.sizeBit:
                return randomNumber
                break

def main():
    generator = BBSGenerator()
    generator.generateNumOfBits()

if __name__ == "__main__":
    main()