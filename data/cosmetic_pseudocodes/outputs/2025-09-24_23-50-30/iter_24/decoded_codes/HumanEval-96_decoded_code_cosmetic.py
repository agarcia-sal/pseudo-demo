from typing import List

def count_up_to(beta: int) -> List[int]:
    gamma: List[int] = []
    xi: int = 2
    while xi < beta:
        theta: bool = True  # affirmative
        omega: int = 2
        while omega < xi and theta:
            if xi % omega == 0:
                theta = False  # negative
            omega += 1
        if theta:
            gamma.append(xi)
        xi += 1
    return gamma