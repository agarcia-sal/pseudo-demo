from typing import Sequence, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(param_alpha: Sequence[T], param_beta: Sequence[T]) -> Sequence[T]:
    counter_omega: int = 0
    iterator_sigma: int = 0
    while iterator_sigma < len(param_alpha):
        element_phi = param_alpha[iterator_sigma]
        temp_length = len(element_phi)
        counter_omega += temp_length
        iterator_sigma += 1

    accumulator_eta: int = 0
    cursor_theta: int = 0
    while cursor_theta < len(param_beta):
        element_delta = param_beta[cursor_theta]
        temp_value = len(element_delta)
        accumulator_eta += temp_value
        cursor_theta += 1

    if counter_omega > accumulator_eta:
        return param_beta
    else:
        return param_alpha