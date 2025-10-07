from typing import Sequence


def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length = len(sequence_of_numbers)
    counter_alpha = 0
    while counter_alpha <= length - 1:
        counter_beta = counter_alpha + 1
        while counter_beta <= length - 1:
            counter_gamma = counter_beta + 1
            while counter_gamma <= length - 1:
                element_one = sequence_of_numbers[counter_alpha]
                element_two = sequence_of_numbers[counter_beta]
                element_three = sequence_of_numbers[counter_gamma]
                summation_temp = element_one + element_two + element_three
                if summation_temp == 0:
                    return True
                counter_gamma += 1
            counter_beta += 1
        counter_alpha += 1
    return False