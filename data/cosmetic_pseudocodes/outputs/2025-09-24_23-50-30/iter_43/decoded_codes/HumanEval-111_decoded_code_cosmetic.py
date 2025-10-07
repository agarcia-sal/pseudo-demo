from typing import Dict


def histogram(parameter_alpha: str) -> Dict[str, int]:
    container_beta: Dict[str, int] = {}
    array_gamma = parameter_alpha.split(' ')
    scalar_delta = 0
    index_epsilon = 0
    length_zeta = len(array_gamma)

    while index_epsilon < length_zeta:
        element_eta = array_gamma[index_epsilon]
        counter_theta = 0
        position_iota = 0
        while position_iota < length_zeta:
            item_kappa = array_gamma[position_iota]
            if item_kappa == element_eta:
                counter_theta += 1
            position_iota += 1
        if counter_theta > scalar_delta and element_eta != "":
            scalar_delta = counter_theta
        index_epsilon += 1

    if scalar_delta > 0:
        index_lambda = 0
        while index_lambda < length_zeta:
            element_mu = array_gamma[index_lambda]
            counter_nu = 0
            position_xi = 0
            while position_xi < length_zeta:
                item_omicron = array_gamma[position_xi]
                if item_omicron == element_mu:
                    counter_nu += 1
                position_xi += 1
            if counter_nu == scalar_delta:
                container_beta[element_mu] = scalar_delta
            index_lambda += 1

    return container_beta