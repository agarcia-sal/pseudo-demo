from typing import List

def solve(int_omega: int) -> str:
    alpha: int = 0
    beta: List[str] = []
    for char_lambda in str(int_omega):
        beta.append(char_lambda)
    for i in range(len(beta)):
        alpha += int(beta[i])
    gamma: str = bin(alpha)
    return gamma[2:]