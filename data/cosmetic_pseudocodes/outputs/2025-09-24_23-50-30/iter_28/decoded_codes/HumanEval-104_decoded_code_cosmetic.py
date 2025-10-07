from typing import List

def unique_digits(parameter_alpha: List[int]) -> List[int]:
    collection_beta: List[int] = []

    def helper_gamma(index_delta: int) -> None:
        if index_delta >= len(parameter_alpha):
            return
        element_epsilon = parameter_alpha[index_delta]

        def all_digits_eta(position_theta: int, value_iota: str) -> bool:
            if position_theta >= len(value_iota):
                return True
            digit_kappa = int(value_iota[position_theta])
            if digit_kappa % 2 != 0:
                return all_digits_eta(position_theta + 1, value_iota)
            else:
                return False

        if all_digits_eta(0, str(element_epsilon)):
            collection_beta.append(element_epsilon)
        helper_gamma(index_delta + 1)

    helper_gamma(0)

    sorted_lambda: List[int] = []
    while collection_beta:
        min_mu = collection_beta[0]
        for item_nu in collection_beta:
            if item_nu < min_mu:
                min_mu = item_nu
        sorted_lambda.append(min_mu)
        temp_xi = [elem_omicron for elem_omicron in collection_beta if elem_omicron != min_mu]
        collection_beta = temp_xi

    return sorted_lambda