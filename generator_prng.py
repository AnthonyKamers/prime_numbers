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
    print(generator.generateNumOfBits())

def main():
    tamanhoBits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    # para cada tamanho em bits, rodar os algoritmos geradores de números
    # pseudo-aleatórios e calcular o tempo de processamento para fazer
    # a planilha com comparações de resultado
    for tamanho in tamanhoBits:
        fib = FibonacciGenerator(sizeBit=tamanho)
        calcularProcessamento(fib, tamanho)
    
    for tamanho in tamanhoBits:
        # fazer dessa forma, pois o gerador de primos com
        # 4096 bits é muito demorado ou não alcança um resultado
        # satisfatório e, como ao usar 2 de 2048 bits, pode-se fazer
        # um número com 4096 bits, vamos fazer dessa forma
        if tamanho == 4096:
            bbs = BBSGenerator(sizeBit=tamanho, sizeBit1=tamanho/2)
        else:
            bbs = BBSGenerator(sizeBit=tamanho)
        calcularProcessamento(bbs, tamanho)

if __name__ == "__main__":
    main()