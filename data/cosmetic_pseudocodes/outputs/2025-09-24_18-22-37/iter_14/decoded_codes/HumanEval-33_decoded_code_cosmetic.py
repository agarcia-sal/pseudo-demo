from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_alpha: List[T]) -> List[T]:
    list_beta: List[T] = []
    index_counter: int = 0

    while index_counter < len(list_alpha):
        list_beta.append(list_alpha[index_counter])
        index_counter += 1

    idx_gamma: int = 0
    extracted_delta: List[T] = []

    while idx_gamma < len(list_beta):
        if (idx_gamma % 3) == 0:
            elem_epsilon = list_beta[idx_gamma]
            extracted_delta.append(elem_epsilon)
        idx_gamma += 1

    delta_sort_temp = extracted_delta
    length_eta = len(delta_sort_temp)
    temp_iota = 0

    while temp_iota < length_eta:
        temp_jeta = 0
        while temp_jeta < (length_eta - temp_iota - 1):
            if delta_sort_temp[temp_jeta] > delta_sort_temp[temp_jeta + 1]:
                temp_kappa = delta_sort_temp[temp_jeta]
                delta_sort_temp[temp_jeta] = delta_sort_temp[temp_jeta + 1]
                delta_sort_temp[temp_jeta + 1] = temp_kappa
            temp_jeta += 1
        temp_iota += 1

    pos_lambda = 0
    iter_mu = 0

    while iter_mu < len(list_beta):
        if (iter_mu % 3) == 0:
            list_beta[iter_mu] = delta_sort_temp[pos_lambda]
            pos_lambda += 1
        iter_mu += 1

    return list_beta