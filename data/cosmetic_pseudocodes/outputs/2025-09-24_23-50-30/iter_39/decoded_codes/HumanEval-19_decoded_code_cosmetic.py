from typing import List, Dict


def sort_numbers(kappa: str) -> str:
    VALUE_MAP: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    def recursive_filter(phi: int, psi: List[str], omega: List[str]) -> List[str]:
        if phi == len(psi):
            return omega
        if psi[phi] != '':
            omega.append(psi[phi])
        return recursive_filter(phi + 1, psi, omega)

    DELTA: List[str] = kappa.split(' ')
    GAMMA: List[str] = recursive_filter(0, DELTA, [])

    def insertion_sort(lambda_list: List[str], mu: int) -> List[str]:
        if mu >= len(lambda_list):
            return lambda_list
        CURRENT = lambda_list[mu]
        NU = mu - 1
        while NU >= 0 and VALUE_MAP[lambda_list[NU]] > VALUE_MAP[CURRENT]:
            lambda_list[NU + 1] = lambda_list[NU]
            NU -= 1
        lambda_list[NU + 1] = CURRENT
        return insertion_sort(lambda_list, mu + 1)

    CLEANED: List[str] = insertion_sort(GAMMA, 1)

    def join_words(words: List[str], idx: int, acc: str) -> str:
        if idx >= len(words):
            return acc
        sep = '' if idx == 0 else ' '
        acc = acc + sep + words[idx]
        return join_words(words, idx + 1, acc)

    return join_words(CLEANED, 0, '')