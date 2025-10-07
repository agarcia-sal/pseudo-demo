from typing import List

def triples_sum_to_zero(array_numbers: List[int]) -> bool:
    length = len(array_numbers)
    pos_alpha = 0
    while pos_alpha <= length - 1:
        pos_beta = pos_alpha + 1
        while pos_beta <= length - 1:
            pos_gamma = pos_beta + 1
            while pos_gamma <= length - 1:
                temp1 = array_numbers[pos_alpha]
                temp2 = array_numbers[pos_beta]
                sum_val = temp1 + temp2
                temp3 = array_numbers[pos_gamma]
                sum_val += temp3
                if not (sum_val != 0):
                    return True
                pos_gamma += 1
            pos_beta += 1
        pos_alpha += 1
    return False