from functools import reduce
from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    alpha: int = 0
    beta: List[int] = []
    for gamma in string_description.split(" "):
        if gamma.isdigit():
            beta.append(int(gamma))
    while alpha < len(beta):
        beta[alpha] = beta[alpha]
        alpha += 1
    return total_number_of_fruits - reduce(lambda acc, val: acc + val, beta, 0)