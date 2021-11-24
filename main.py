from PrimeNumbers.MillerRabin import MillerRabin
from PrimeNumbers.SolovayStrassen import SolovayStressen
from PRNG.FibonacciGenerator import FibonacciGenerator
from PRNG.BBSGenerator import BBSGenerator
from utils import *

@profile
def calcularProcessamento(generator, tamanho):
    print(tamanho)
    k = 2
    while True:
        randomNumber = generator.generateNumOfBits()
        if MillerRabin(randomNumber, k) == True:
            print(randomNumber)
            break

def main():
    tamanhoBits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    for tamanho in tamanhoBits:
        generator = FibonacciGenerator(sizeBit=tamanho)
        calcularProcessamento(generator, tamanho)

if __name__ == "__main__":
    main()