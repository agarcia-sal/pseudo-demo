from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    counter_alpha: int = 0
    length: int = len(sequence_of_numbers)
    while True:
        if counter_alpha > length - 1:
            break
        counter_beta: int = counter_alpha + 1
        while True:
            if counter_beta > length - 1:
                break
            counter_gamma: int = counter_beta + 1
            while counter_gamma <= length - 1:
                first_element: int = sequence_of_numbers[counter_alpha]
                second_element: int = sequence_of_numbers[counter_beta]
                third_element: int = sequence_of_numbers[counter_gamma]
                total_sum: int = first_element + second_element + third_element
                if total_sum == 0:
                    return True
                counter_gamma += 1
            counter_beta += 1
        counter_alpha += 1
    return False