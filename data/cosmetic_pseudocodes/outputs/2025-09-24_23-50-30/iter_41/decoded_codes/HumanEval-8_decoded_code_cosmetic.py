from typing import Sequence, Tuple, Union

def sum_product(container_param: Sequence[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    return accumulate(container_param, 0, len(container_param), 0, 1)

def accumulate(
    seq_param: Sequence[Union[int, float]],
    idx_param: int,
    limit_param: int,
    acc_sum: Union[int, float],
    acc_prod: Union[int, float]
) -> Tuple[Union[int, float], Union[int, float]]:
    if idx_param >= limit_param:
        return acc_sum, acc_prod
    return accumulate(
        seq_param,
        idx_param + 1,
        limit_param,
        acc_sum + seq_param[idx_param],
        acc_prod * seq_param[idx_param]
    )