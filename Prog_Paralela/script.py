from multiprocessing import Process

def pi_naive(start, end, step):
    soma = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        soma += 4.0 / (1.0 + x * x)
    return soma

if __name__ == "__main__":
    num_steps = 100_000_000
    step = 1.0 / num_steps

    n_proc = 4
    chunk = num_steps // n_proc

    processos = []

    for i in range(n_proc):
        inicio = i * chunk
        fim = num_steps if i == n_proc - 1 else (i + 1) * chunk

        processos.append(
            Process(
                target=pi_naive,
                args=(inicio, fim, step)
            )
        )

    for p in processos:
        p.start()

    for p in processos:
        p.join()

    print("FIM")
