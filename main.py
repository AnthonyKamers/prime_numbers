import time
from PrimeNumbers.MillerRabin import MillerRabin
from PrimeNumbers.SolovayStrassen import SolovayStressen
from PRNG.FibonacciGenerator import FibonacciGenerator
from PRNG.BBSGenerator import BBSGenerator

# calcular o tempo de uma função
# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
def profile(fct):
  def wrapper(*args, **kw):
    start_time = time.time()
    ret = fct(*args, **kw)
    print("{} {} {} return {} in {} seconds".format(args[0].__class__.__name__,
                                                    args[0].__class__.__module__,
                                                    fct.__name__,
                                                    ret,
                                                    time.time() - start_time))
    return ret
  return wrapper

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