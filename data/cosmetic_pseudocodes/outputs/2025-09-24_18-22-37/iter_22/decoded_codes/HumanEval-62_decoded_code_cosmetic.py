from typing import List

def derivative(signal: List[float]) -> List[float]:
    result: List[float] = []
    index: int = 1
    while index < len(signal):
        multiplier: int = index
        term: float = signal[index] * multiplier
        result.append(term)
        index += 1
    return result