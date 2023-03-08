from random import randint, random
from typing import List, Tuple, Callable
from string import maketrans



def cruzamento_pais(pai1: str, pai2: str, taxa_cruzamento: float) -> Tuple[]:
    if random() <= taxa_cruzamento:
        ponto_cruzamento = randint(1, len(pai1))
        filho_1: str = pai1[:ponto_cruzamento] + pai2[ponto_cruzamento:]
        filho_2: str = pai2[:ponto_cruzamento] + pai1[ponto_cruzamento:]
        return filho1, filho2
    return pai1, pai2
#ok


def cruzamento()



def mutacao_individuo(filho: str, taxa_mutacao: float) -> str:
    for i, s in enumerate(filho):
        if random() <= taxa_mutacao:
            filho[i] = str((int(s) + 1) % 2)
            return filho
# ok


def mutacao(filhos: List[str], taxa_mutacao: float) -> List[str]:
    for i, ind in




def torneio(aptidao: List[float]) -> int:
    pai1 = randint(len(aptidao))
    pai2 = randint(len(aptidao))
    return pai1 if aptidao[pai1] > aptidao[pai2] else pai2
#ok


def selecao_pais(pop: List[str], sel_func: Callable) -> List[str]:
    lista_pais: List[str] = [None] * len(pop)
    for i in range(len(pop)):
        lista_pais[i] = sel_func(aptidao)
    return lista_pais
#ok

def selecao_sobreviventes(pop: List[str], apt_pop: List[float], filhos: List[str], apt_filhos: List[float]) -> List[str]:
    return filhos
#substituicao geracional ok

def pop_inicial(tamanho_pop: int, n_genes: int) -> List[str]:
    pop: List[str] = [""] * tamanho_pop
    for i in range(tamanho_pop):
        individuo = "".join([str(randint(0, 1)) for _ in range(n_genes)])
        pop[i] = individuo
    return pop
#ok

def evolucao(tamanho_pop: int, n_genes: int, taxa_cruzamento: float, taxa_mutacao: float, n_geracoes: int) -> List[str]:
    pop = pop_inicial(tamanho_pop, n_genes)
    apt: List[float] = aptidao(pop)
    for geracao in range(n_geracoes):
        pais = selecao_pais(pop, apt, torneio)
        filhos = cruzamento(pais, taxa_cruzamento)
        filhos = mutacao(filhos, taxa_mutacao)
        apt_filhos = aptidao(filhos)
        pop, apt = selecao_sobreviventes(pop, apt, filhos, apt_filhos)
    return pop, apt
#ok
