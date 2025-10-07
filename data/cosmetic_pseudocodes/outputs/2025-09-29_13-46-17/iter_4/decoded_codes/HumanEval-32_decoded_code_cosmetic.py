from typing import List, Tuple

def poly(list_of_coefficients: List[float], point: float) -> float:
    def power_accumulate(counter: int, acc: float) -> float:
        if counter == len(list_of_coefficients):
            return acc
        coeff_element = list_of_coefficients[counter]
        updated_acc = acc + coeff_element * point ** counter
        return power_accumulate(counter + 1, updated_acc)
    return power_accumulate(0, 0.0)

def find_zero(list_of_coefficients: List[float]) -> float:
    alpha: float = -1.0
    omega: float = 1.0

    def expand_bounds(a: float, b: float) -> Tuple[float, float]:
        eval_a = poly(list_of_coefficients, a)
        eval_b = poly(list_of_coefficients, b)
        if (eval_a * eval_b) > 0:
            return expand_bounds(a * 2.0, b * 2.0)
        return (a, b)

    lower_bound, upper_bound = expand_bounds(alpha, omega)

    def bisect(low: float, high: float) -> float:
        delta = high - low
        if not (delta > 1e-10):
            return low
        mid = (low + high) / 2.0
        eval_mid = poly(list_of_coefficients, mid)
        eval_low = poly(list_of_coefficients, low)
        if (eval_mid * eval_low) > 0:
            return bisect(mid, high)
        else:
            return bisect(low, mid)

    return bisect(lower_bound, upper_bound)