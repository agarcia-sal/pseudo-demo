from typing import List

def derivative(list_of_coefficients: List[int]) -> List[int]:
    def _recurse_lambda(limbs: List[int], idx: int, acc: List[int]) -> List[int]:
        if not limbs:
            return acc
        return _recurse_lambda(limbs[1:], idx + 1, acc + [limbs[0] * idx])
    return _recurse_lambda(list_of_coefficients[1:], 1, [])