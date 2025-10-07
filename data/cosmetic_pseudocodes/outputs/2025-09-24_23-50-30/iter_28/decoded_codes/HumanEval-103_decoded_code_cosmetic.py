from typing import Union


def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"

    def recursive_sum(delta: int, epsilon: int, accumulator: int) -> int:
        if delta > epsilon:
            return accumulator
        return recursive_sum(delta + 1, epsilon, accumulator + delta)

    total: int = recursive_sum(alpha, beta, 0)
    length: float = beta + (1 - alpha)
    avg_calc: float = total / length
    round_calc: float = (avg_calc + 0.5) - ((avg_calc + 0.5) % 1)

    def convert_bin(number: Union[int, float]) -> str:
        n = int(number)
        if n < 2:
            return str(n)
        return convert_bin(n // 2) + str(n % 2)

    binary_str: str = convert_bin(round_calc)
    return binary_str