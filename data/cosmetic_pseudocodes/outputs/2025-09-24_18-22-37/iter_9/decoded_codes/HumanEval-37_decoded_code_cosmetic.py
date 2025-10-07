from typing import List, TypeVar

T = TypeVar('T')

def sort_even(parameter_alpha: List[T]) -> List[T]:
    temp_beta: List[T] = []
    temp_gamma: List[T] = []
    index_delta = 0
    while index_delta < len(parameter_alpha):
        if index_delta % 2 == 0:
            temp_beta.append(parameter_alpha[index_delta])
        else:
            temp_gamma.append(parameter_alpha[index_delta])
        index_delta += 1

    index_epsilon = 0
    temp_theta = len(temp_beta)
    while index_epsilon < temp_theta - 1:
        index_zeta = index_epsilon
        while index_zeta < temp_theta - 1:
            if not (temp_beta[index_zeta] <= temp_beta[index_zeta + 1]):
                temp_eta = temp_beta[index_zeta]
                temp_beta[index_zeta] = temp_beta[index_zeta + 1]
                temp_beta[index_zeta + 1] = temp_eta
            index_zeta += 1
        index_epsilon += 1

    result_list: List[T] = []
    index_iota = 0
    while index_iota < len(temp_gamma):
        result_list.append(temp_beta[index_iota])
        result_list.append(temp_gamma[index_iota])
        index_iota += 1

    if not (len(temp_beta) <= len(temp_gamma)):
        result_list.append(temp_beta[len(temp_beta) - 1])

    return result_list