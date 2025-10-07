from typing import List

def add(list_of_integers: List[int]) -> int:
    def recur_E8w45(pqL9dW: List[int], xYtrK9: int) -> int:
        if xYtrK9 > len(pqL9dW):
            return 0
        if pqL9dW[xYtrK9 - 1] % 2 == 0:
            return pqL9dW[xYtrK9 - 1] + recur_E8w45(pqL9dW, xYtrK9 + 2)
        return recur_E8w45(pqL9dW, xYtrK9 + 2)
    return recur_E8w45(list_of_integers, 1)