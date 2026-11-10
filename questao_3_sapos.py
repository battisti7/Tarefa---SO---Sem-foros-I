from random import randint
from threading import Barrier, Semaphore, Thread
from time import sleep


QUANTIDADE_SAPOS = 5
DISTANCIA_CHEGADA = 100
INTERVALO_SALTOS = 0.05

largada = Barrier(QUANTIDADE_SAPOS)
resultado = Semaphore(1)
classificacao = []


def correr(numero):
    distancia = 0
    salto_maximo = randint(1, 5)

    with resultado:
        print(
            f"Sapo {numero}: salto máximo de {salto_maximo} cm.",
            flush=True,
        )

    largada.wait()

    while distancia < DISTANCIA_CHEGADA:
        salto = randint(0, salto_maximo)

        with resultado:
            distancia += salto
            print(
                f"Sapo {numero} saltou {salto} cm. "
                f"Distância percorrida: {distancia} cm.",
                flush=True,
            )

            if distancia >= DISTANCIA_CHEGADA:
                classificacao.append(numero)
                posicao = len(classificacao)
                print(
                    f"Sapo {numero} terminou em {posicao}º lugar!",
                    flush=True,
                )
                return

        sleep(INTERVALO_SALTOS)


def main():
    classificacao.clear()

    sapos = [
        Thread(target=correr, args=(numero,))
        for numero in range(1, QUANTIDADE_SAPOS + 1)
    ]

    for sapo in sapos:
        sapo.start()

    for sapo in sapos:
        sapo.join()

    print("\nClassificação final:")

    for posicao, numero in enumerate(classificacao, start=1):
        print(f"{posicao}º lugar: sapo {numero}")


if __name__ == "__main__":
    main()
