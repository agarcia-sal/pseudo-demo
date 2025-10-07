from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    counter_alpha = 0
    counter_beta = 0
    index_gamma = 0
    while index_gamma < len(list_one):
        value_delta = list_one[index_gamma]
        remainder_epsilon = value_delta % 2
        if remainder_epsilon == 1:
            counter_alpha += 1
        index_gamma += 1
    index_zeta = 0
    while index_zeta < len(list_two):
        value_eta = list_two[index_zeta]
        parity_theta = value_eta % 2
        if parity_theta == 0:
            counter_beta += 1
        index_zeta += 1
    if counter_beta >= counter_alpha:
        return "YES"
    else:
        return "NO"