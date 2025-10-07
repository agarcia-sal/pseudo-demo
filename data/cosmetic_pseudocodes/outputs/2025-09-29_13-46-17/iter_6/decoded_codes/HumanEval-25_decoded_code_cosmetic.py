from typing import List

def factorize(integer_n: int) -> List[int]:
    tabulated_factors: List[int] = []
    factor_candidate: int = 2
    upper_limit: int = int(integer_n**0.5) + 1

    def recursiveDivide(number: int, candidate: int, boundary: int, collected: List[int]) -> List[int]:
        if candidate > boundary:
            return collected + ([number] if number > 1 else [])
        elif number % candidate == 0:
            return recursiveDivide(number // candidate, candidate, boundary, collected + [candidate])
        else:
            return recursiveDivide(number, candidate + 1, boundary, collected)

    return recursiveDivide(integer_n, factor_candidate, upper_limit, tabulated_factors)