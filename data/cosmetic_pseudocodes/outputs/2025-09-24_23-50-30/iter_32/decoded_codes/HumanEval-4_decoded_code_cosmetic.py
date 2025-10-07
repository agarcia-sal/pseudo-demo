from typing import Sequence


def mean_absolute_deviation(identifier_1: Sequence[float]) -> float:
    identifier_2: float = 0.0
    identifier_3: int = 0
    identifier_4: int = len(identifier_1)
    for identifier_5 in range(identifier_4):
        identifier_2 += identifier_1[identifier_5]
    identifier_6: float = identifier_2 / identifier_4
    while identifier_3 < identifier_4:
        identifier_2 += abs(identifier_1[identifier_3] - identifier_6)
        identifier_3 += 1
    identifier_7: float = identifier_2 / identifier_4
    return identifier_7