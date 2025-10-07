from typing import List

def parse_music(beta: str) -> List[int]:
    gamma = {'.|': 1, 'o|': 2, 'o': 4}
    delta = beta.split(' ')
    epsilon: List[int] = []
    for zeta in range(len(delta)):
        if delta[zeta] != '':
            epsilon.append(gamma[delta[zeta]])
    return epsilon