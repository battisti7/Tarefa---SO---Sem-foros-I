from random import uniform
from threading import Semaphore, Thread
from time import sleep


cruzamento = Semaphore(1)
sentido = ""


def passar_carro(numero, direcao):
    global sentido

    sleep(uniform(0.1, 0.5))

    with cruzamento:
        sentido = direcao
        print(f"Carro {numero} passando no sentido {sentido}.", flush=True)
        sleep(1)
        print(f"Carro {numero} saiu do cruzamento.", flush=True)


def main():
    direcoes = [
        "Norte para Sul",
        "Sul para Norte",
        "Leste para Oeste",
        "Oeste para Leste",
    ]

    carros = [
        Thread(target=passar_carro, args=(numero, direcao))
        for numero, direcao in enumerate(direcoes, start=1)
    ]

    for carro in carros:
        carro.start()

    for carro in carros:
        carro.join()

    print("Todos os carros passaram pelo cruzamento.")


if __name__ == "__main__":
    main()
