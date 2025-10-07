from typing import List, Union

def pluck(beta: List[int]) -> Union[List[int], List[Union[int, int]]]:
    if len(beta) == 0:
        return []
    else:
        gamma: List[int] = [delta for delta in beta if delta % 2 == 0]
        if len(gamma) == 0:
            return []
        else:
            epsilon: int = float('inf')
            zeta: int = -1
            eta: int = 0
            while eta < len(beta):
                if beta[eta] == min(gamma):
                    epsilon = beta[eta]
                    zeta = eta
                    break
                eta += 1
            return [epsilon, zeta]