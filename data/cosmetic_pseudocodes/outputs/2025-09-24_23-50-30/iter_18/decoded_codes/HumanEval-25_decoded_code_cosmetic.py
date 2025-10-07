from typing import List


def factorize(integer_n: int) -> List[int]:
    factors_dict: dict[int, bool] = {}
    candidate_divisor: int = 2
    limit_value: float = integer_n ** 0.5
    upper_bound: int = int(limit_value) + 1

    while True:
        if candidate_divisor > upper_bound:
            break

        if (integer_n // candidate_divisor) * candidate_divisor == integer_n:
            factors_dict[candidate_divisor] = True
            integer_n //= candidate_divisor
            limit_value = integer_n ** 0.5
            upper_bound = int(limit_value) + 1
            continue
        else:
            candidate_divisor += 1

    if integer_n <= 1:
        return list(factors_dict.keys())
    else:
        return list(factors_dict.keys()) + [integer_n]