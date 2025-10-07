from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    alpha = string_s.split(' ')
    beta: List[str] = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for gamma in range(len(alpha)):
        delta = 0
        for epsilon in range(len(alpha[gamma])):
            phi = alpha[gamma][epsilon].lower()
            if phi not in vowels:
                delta += 1
        if delta == natural_number_n:
            beta.append(alpha[gamma])
    return beta