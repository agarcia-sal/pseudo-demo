from typing import List


def count_up_to(w: int) -> List[int]:
    X: List[int] = []
    V: int = 2
    while V < w:
        U: bool = True
        Y: int = 2
        while Y < V:
            if not (V % Y != 0):  # i.e., if V % Y == 0
                U = False
                Y = V  # exit inner loop
            else:
                Y += 1
        if U:
            X.append(V)
        # else: no action needed; V remains the same here
        V += 1
    return X