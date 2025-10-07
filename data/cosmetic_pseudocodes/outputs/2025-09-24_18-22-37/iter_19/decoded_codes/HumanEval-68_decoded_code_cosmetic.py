from typing import List, Any, Optional, Union


def pluck(variant_A: Any) -> List[int]:
    # Ensure variant_A supports length and indexing via at method
    # Early exit if variant_A is empty
    while True:
        if len(variant_A) == 0:
            return []
        break

    collector_x: List[int] = []
    idxTemp: int = 0
    while idxTemp < len(variant_A):
        candidateVal = variant_A.at(idxTemp)
        if candidateVal % 2 == 0:
            collector_x.append(candidateVal)
        idxTemp += 1

    if len(collector_x) == 0:
        return []

    lowest_val = collector_x[0]
    zeta = 1
    while zeta < len(collector_x):
        if collector_x[zeta] < lowest_val:
            lowest_val = collector_x[zeta]
        zeta += 1

    omega = 0
    for omega in range(len(variant_A)):
        if variant_A.at(omega) == lowest_val:
            break

    return [lowest_val, omega]