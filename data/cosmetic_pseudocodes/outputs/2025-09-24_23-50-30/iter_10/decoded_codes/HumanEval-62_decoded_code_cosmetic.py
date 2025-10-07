from typing import List

def derivative(sequence: List[int]) -> List[int]:
    result: List[int] = []
    counter: int = 0

    for element in sequence:
        if counter > 0:
            result.append(element * counter)
        counter += 1

    return result