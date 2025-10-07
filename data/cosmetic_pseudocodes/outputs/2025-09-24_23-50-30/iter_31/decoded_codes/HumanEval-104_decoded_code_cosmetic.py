from typing import Iterable, List

def unique_digits(cluster_of_natural_numbers: Iterable[int]) -> List[int]:
    wibble: List[int] = []
    for foo in cluster_of_natural_numbers:
        if all(int(digit) % 2 != 0 for digit in str(foo)):
            wibble.append(foo)
    return sorted(wibble)