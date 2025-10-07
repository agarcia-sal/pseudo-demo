from typing import List

def derivative(sequence_of_numbers: List[float]) -> List[float]:
    result_sequence: List[float] = []
    counter: int = 0
    while counter < len(sequence_of_numbers):
        if counter != 0:
            current_product: float = counter * sequence_of_numbers[counter]
            result_sequence.append(current_product)
        counter += 1
    return result_sequence