from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    alpha: List[int] = sorted(array_of_integers)

    def compute_ones(element: int) -> int:
        bitstring = bin(element)[2:]  # binary representation without '0b' prefix
        return sum(1 for char in bitstring if char == '1')

    beta: List[int] = sorted(alpha, key=compute_ones)
    return beta