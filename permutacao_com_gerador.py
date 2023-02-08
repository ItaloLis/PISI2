def permutacao_gerador(lista):
    if len(lista) <= 1:
        yield lista
        return
    for i, atual in enumerate(lista):
        elementos_restantes = lista[:i] + lista[i + 1:]
        for p in permutacao_gerador(elementos_restantes):
            yield [atual] + p


def main():
    pontos_de_entrega = list(range(4))
    for i, p in enumerate(permutacao_gerador(pontos_de_entrega)):
        print(f"Permutacao {i+1} == {p}")

main()
