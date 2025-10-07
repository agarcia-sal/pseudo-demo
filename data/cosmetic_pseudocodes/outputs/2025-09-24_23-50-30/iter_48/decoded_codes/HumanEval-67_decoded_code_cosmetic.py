from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    W: List[int] = []
    X: List[str] = string_description.split(' ')
    Y: int = 0
    while Y < len(X):
        Z: str = X[Y]
        if not (Z < "0" or Z > "9"):
            W.append(int(Z))
        Y += 1
    V: int = 0
    U: int = 0
    while U < len(W):
        V += W[U]
        U += 1
    return total_number_of_fruits - V