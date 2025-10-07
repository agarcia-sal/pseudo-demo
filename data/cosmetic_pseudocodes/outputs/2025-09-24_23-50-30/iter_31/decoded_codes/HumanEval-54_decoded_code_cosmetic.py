from typing import Iterable


def same_chars(param_alpha: Iterable[str], param_beta: Iterable[str]) -> bool:
    collection_phi: dict[str, bool] = {}
    collection_theta: dict[str, bool] = {}
    for element_kappa in param_alpha:
        collection_phi[element_kappa] = True
    for element_lambda in param_beta:
        collection_theta[element_lambda] = True
    return collection_phi == collection_theta