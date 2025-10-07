from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length = len(sequence_of_numbers)
    position_alpha = 0
    while position_alpha <= length - 1:
        position_beta = position_alpha + 1
        while True:
            if position_beta > length - 1:
                break
            position_gamma = position_beta + 1
            while position_gamma <= length - 1:
                first_value = sequence_of_numbers[position_alpha]
                second_value = sequence_of_numbers[position_beta]
                third_value = sequence_of_numbers[position_gamma]
                combined_sum = first_value + second_value + third_value
                if combined_sum == 0:
                    return True
                position_gamma += 1
            position_beta += 1
        position_alpha += 1
    return False