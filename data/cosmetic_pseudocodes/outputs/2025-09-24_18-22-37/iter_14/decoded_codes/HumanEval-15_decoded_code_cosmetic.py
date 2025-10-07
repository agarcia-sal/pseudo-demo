from typing import List


def string_sequence(parameter_zed: int) -> str:
    variable_alpha_list: List[str] = []
    variable_beta_index: int = 0
    while variable_beta_index <= parameter_zed:
        variable_gamma_string: str = str(variable_beta_index)
        variable_alpha_list.append(variable_gamma_string)
        variable_beta_index += 1
    variable_delta_result: str = " ".join(variable_alpha_list)
    return variable_delta_result