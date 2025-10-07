from typing import List

def f(parameter_m: int) -> List[int]:
    accumulator_X: List[int] = []
    counter_P: int = 1
    while counter_P <= parameter_m:
        if counter_P % 2 == 0:
            product_Q: int = 1
            iterator_R: int = 1
            while iterator_R <= counter_P:
                product_Q *= iterator_R
                iterator_R += 1
            accumulator_X.append(product_Q)
        else:
            sum_S: int = 0
            index_T: int = 1
            while index_T <= counter_P:
                sum_S += index_T
                index_T += 1
            accumulator_X.append(sum_S)
        counter_P += 1
    return accumulator_X