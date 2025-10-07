from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    n = len(sequence_of_numbers)
    if n < 3:
        return False
    primary_pointer = 0
    while primary_pointer < n - 1:
        secondary_pointer = primary_pointer + 1
        while secondary_pointer < n - 1:
            tertiary_pointer = secondary_pointer + 1
            while tertiary_pointer < n - 1:
                first_value = sequence_of_numbers[primary_pointer]
                second_value = sequence_of_numbers[secondary_pointer]
                third_value = sequence_of_numbers[tertiary_pointer]
                sum_of_three = first_value + second_value + third_value
                if sum_of_three == 0:
                    return True
                tertiary_pointer += 1
            secondary_pointer += 1
        primary_pointer += 1
    return False