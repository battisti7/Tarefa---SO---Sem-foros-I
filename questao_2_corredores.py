from random import uniform
from threading import Semaphore, Thread
from time import sleep


DISTANCIA_CORREDOR = 200

porta = Semaphore(1)
console = Semaphore(1)


def mostrar(mensagem):
    with console:
        print(mensagem, flush=True)


def caminhar(numero):
    velocidade = uniform(4, 6)
    tempo_caminhada = DISTANCIA_CORREDOR / velocidade

    mostrar(
        f"Pessoa {numero} caminhando a {velocidade:.2f} m/s. "
        f"Tempo para percorrer os 200 m: {tempo_caminhada:.2f} s."
    )

    sleep(tempo_caminhada)
    mostrar(f"Pessoa {numero} chegou à porta e está aguardando.")

    with porta:
        tempo_travessia = uniform(1, 2)
        mostrar(
            f"Pessoa {numero} abrindo e cruzando a porta. "
            f"Tempo: {tempo_travessia:.2f} s."
        )
        sleep(tempo_travessia)
        mostrar(f"Pessoa {numero} terminou de cruzar a porta.")


def main():
    pessoas = [
        Thread(target=caminhar, args=(numero,))
        for numero in range(1, 5)
    ]

    for pessoa in pessoas:
        pessoa.start()

    for pessoa in pessoas:
        pessoa.join()

    print("Todas as pessoas atravessaram a porta.")


if __name__ == "__main__":
    main()
