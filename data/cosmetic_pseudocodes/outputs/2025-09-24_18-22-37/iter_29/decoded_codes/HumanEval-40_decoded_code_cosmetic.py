from typing import List


def triples_sum_to_zero(array_of_numbers: List[int]) -> bool:
    length = len(array_of_numbers)
    a_pos = 0
    while a_pos < length:
        b_pos = a_pos + 1
        while b_pos < length:
            c_pos = b_pos + 1
            while c_pos < length:
                first_val = array_of_numbers[a_pos]
                second_val = array_of_numbers[b_pos]
                third_val = array_of_numbers[c_pos]
                total_sum = first_val + second_val + third_val
                if not (total_sum != 0):
                    return True
                c_pos += 1
            b_pos += 1
        a_pos += 1
    return False