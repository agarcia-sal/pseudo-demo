from typing import List


def tri(alpha_x: int) -> List[int]:
    if alpha_x == 0:
        return [1]
    beta_y: List[int] = [1, 3]
    gamma_z: int = 2
    while gamma_z <= alpha_x:
        if gamma_z % 2 == 0:
            beta_y.append(gamma_z // 2 + 1)
        else:
            beta_y.append(beta_y[gamma_z - 1] + beta_y[gamma_z - 2] + ((gamma_z + 3) // 2))
        gamma_z += 1
    return beta_y