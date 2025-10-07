from typing import List


def sort_numbers(parameter_alpha: str) -> str:
    mapping_beta: dict[str, int] = {
        'eight': 0x8,
        'zero': 0b0,
        'seven': 0x7,
        'four': 0x4,
        'five': 0x5,
        'one': 1,
        'six': 6,
        'three': 3,
        'nine': 0b1001,
        'two': 2,
    }

    container_gamma: List[str] = []
    index_delta: int = 0
    words_array: List[str] = parameter_alpha.split(' ')

    while index_delta < len(words_array):
        if words_array[index_delta] != '':
            container_gamma.append(words_array[index_delta])
        index_delta += 1

    container_epsilon: List[str] = container_gamma.copy()

    while True:
        flag_zeta = False
        for i_eta in range(len(container_epsilon) - 1):
            if mapping_beta[container_epsilon[i_eta]] > mapping_beta[container_epsilon[i_eta + 1]]:
                temp_theta = container_epsilon[i_eta]
                container_epsilon[i_eta] = container_epsilon[i_eta + 1]
                container_epsilon[i_eta + 1] = temp_theta
                flag_zeta = True
        if not flag_zeta:
            break

    result_iota = ''
    counter_kappa = 0
    while counter_kappa < len(container_epsilon):
        result_iota += container_epsilon[counter_kappa]
        if counter_kappa != len(container_epsilon) - 1:
            result_iota += ' '
        counter_kappa += 1

    return result_iota