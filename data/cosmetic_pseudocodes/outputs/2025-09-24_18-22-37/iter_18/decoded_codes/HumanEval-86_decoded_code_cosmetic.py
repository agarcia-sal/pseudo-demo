from typing import List

def anti_shuffle(input_string: str) -> str:
    var_alpha: List[str] = input_string.split(" ")
    var_beta: List[str] = []
    index_omega: int = 0
    length_delta: int = len(var_alpha)

    while index_omega < length_delta:
        var_xi: str = var_alpha[index_omega]
        temp_gamma: List[str] = [char_kappa for char_kappa in var_xi]

        # Bubble sort ascending by ASCII values
        while True:
            swapped: bool = False
            i_lambda: int = 0
            while i_lambda < len(temp_gamma) - 1:
                if temp_gamma[i_lambda] > temp_gamma[i_lambda + 1]:
                    temp_gamma[i_lambda], temp_gamma[i_lambda + 1] = temp_gamma[i_lambda + 1], temp_gamma[i_lambda]
                    swapped = True
                i_lambda += 1
            if not swapped:
                break

        assembled_word: str = "".join(temp_gamma)
        var_beta.append(assembled_word)
        index_omega += 1

    if len(var_beta) == 0:
        return ""

    var_result: str = var_beta[0]
    idx_sigma: int = 1

    while idx_sigma < len(var_beta):
        var_result += " " + var_beta[idx_sigma]
        idx_sigma += 1

    return var_result