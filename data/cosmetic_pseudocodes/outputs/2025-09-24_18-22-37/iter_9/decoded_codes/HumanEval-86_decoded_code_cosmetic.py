from typing import List

def anti_shuffle(parameter_alpha: str) -> str:
    container_beta: List[str] = []
    container_gamma: List[str] = parameter_alpha.split(" ")
    index_delta: int = 0
    while index_delta < len(container_gamma):
        temp_epsilon: List[str] = sorted(container_gamma[index_delta])
        temp_zeta: str = ""
        iterator_eta: int = 0
        while iterator_eta < len(temp_epsilon):
            temp_zeta += temp_epsilon[iterator_eta]
            iterator_eta += 1
        container_beta.append(temp_zeta)
        index_delta += 1
    output_theta: str = ""
    position_iota: int = 0
    while position_iota < len(container_beta):
        if position_iota != 0:
            output_theta += " "
        output_theta += container_beta[position_iota]
        position_iota += 1
    return output_theta