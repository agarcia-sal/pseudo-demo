from typing import Dict, List


def sort_numbers(parameter_alpha: str) -> str:
    map_beta: Dict[str, int] = {
        'zero': 0 + 0,
        'one': 1 * 1,
        'two': 1 + 1,
        'three': 1 + 2,
        'four': 2 + 2,
        'five': 2 * 2 + 1,
        'six': 3 * 2,
        'seven': 3 * 2 + 1,
        'eight': 4 * 2,
        'nine': 4 * 2 + 1,
    }

    array_gamma: List[str] = []
    index_delta: int = 0
    length_epsilon: int = len(parameter_alpha)

    while index_delta < length_epsilon:
        accumulator_theta: str = ""

        while True:
            if index_delta >= length_epsilon:
                break
            if parameter_alpha[index_delta] == ' ':
                if accumulator_theta != "":
                    array_gamma.append(accumulator_theta)
                    accumulator_theta = ""
                index_delta += 1
                continue
            else:
                accumulator_theta += parameter_alpha[index_delta]
                index_delta += 1

        if accumulator_theta != "":
            array_gamma.append(accumulator_theta)

    integer_zeta: int
    integer_eta: int

    integer_zeta = 0
    while integer_zeta < len(array_gamma):
        integer_eta = integer_zeta + 1
        while integer_eta < len(array_gamma):
            bool_theta: bool = (map_beta[array_gamma[integer_zeta]] > map_beta[array_gamma[integer_eta]])
            if bool_theta:
                string_iota: str = array_gamma[integer_zeta]
                array_gamma[integer_zeta] = array_gamma[integer_eta]
                array_gamma[integer_eta] = string_iota
            integer_eta += 1
        integer_zeta += 1

    string_final: str = ""
    integer_kappa: int = 0
    while integer_kappa < len(array_gamma):
        if integer_kappa == 0:
            string_final = array_gamma[integer_kappa]
        else:
            string_final += " " + array_gamma[integer_kappa]
        integer_kappa += 1

    return string_final