from typing import List, Dict

def f(integer_n: int) -> List[int]:
    acc_result: Dict[int, int] = {index: 0 for index in range(1, integer_n + 1)}
    idx: int = 1
    while idx <= integer_n:
        if idx % 2 == 0:
            prod_acc: int = 1
            factor_itr: int = 1
            while factor_itr <= idx:
                prod_acc *= factor_itr
                factor_itr += 1
            acc_result[idx] = prod_acc
        else:
            sum_acc: int = 0
            term_itr: int = 1
            while term_itr <= idx:
                sum_acc += term_itr
                term_itr += 1
            acc_result[idx] = sum_acc
        idx += 1
    return [acc_result[x] for x in range(1, integer_n + 1)]