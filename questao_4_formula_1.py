from random import uniform
from threading import Semaphore, Thread
from time import sleep


QUANTIDADE_EQUIPES = 7
CARROS_POR_EQUIPE = 2
TOTAL_VOLTAS = 3

pista = Semaphore(5)
equipes = [Semaphore(1) for _ in range(QUANTIDADE_EQUIPES)]
console = Semaphore(1)


def mostrar(mensagem):
    with console:
        print(mensagem, flush=True)


def treinar(equipe, carro):
    mostrar(f"Equipe {equipe}, carro {carro}: aguardando para treinar.")

    with equipes[equipe - 1]:
        with pista:
            mostrar(f"Equipe {equipe}, carro {carro}: entrou na pista.")

            for volta in range(1, TOTAL_VOLTAS + 1):
                tempo_volta = uniform(1, 3)
                sleep(tempo_volta)
                mostrar(
                    f"Equipe {equipe}, carro {carro}: "
                    f"volta {volta} em {tempo_volta:.2f} s."
                )

            mostrar(f"Equipe {equipe}, carro {carro}: saiu da pista.")


def main():
    carros = [
        Thread(target=treinar, args=(equipe, carro))
        for equipe in range(1, QUANTIDADE_EQUIPES + 1)
        for carro in range(1, CARROS_POR_EQUIPE + 1)
    ]

    for carro in carros:
        carro.start()

    for carro in carros:
        carro.join()

    print("Treino concluído: os 14 carros completaram 3 voltas cada.")


if __name__ == "__main__":
    main()
