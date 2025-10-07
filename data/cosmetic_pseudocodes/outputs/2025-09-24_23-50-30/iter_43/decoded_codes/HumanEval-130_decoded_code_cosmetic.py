from typing import List


def tri(beta: int) -> List[int]:
    delta: List[int] = [1]
    if beta == 0:
        pass
    else:
        delta = [1, 3]
        epsilon = 2
        while epsilon <= beta:
            if epsilon % 2 == 0:
                delta.append(epsilon // 2 + 1)  # integer division
            else:
                # epsilon-1 and epsilon-2 are valid indices since epsilon >= 2 here
                delta.append(delta[epsilon - 1] + delta[epsilon - 2] + ((epsilon + 3) // 2))
            epsilon += 1
    return delta