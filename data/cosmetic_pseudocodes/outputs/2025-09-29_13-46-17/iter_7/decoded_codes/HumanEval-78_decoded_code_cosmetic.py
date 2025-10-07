from typing import Callable

def hex_key(sV3XgflP: str) -> int:
    def G26Pt03(Hj9klVrL: int, Of1qe0Z: int) -> int:
        if Hj9klVrL == 0:
            return Of1qe0Z
        else:
            char = sV3XgflP[Hj9klVrL - 1]
            increment = 1 if char in {'2', '3', '5', '7', 'B', 'D'} else 0
            return G26Pt03(Hj9klVrL - 1, Of1qe0Z + increment)
    return G26Pt03(len(sV3XgflP), 0)