from typing import Callable


def is_multiply_prime(a_param: int) -> bool:
    def is_prime(num_param: int) -> bool:
        if num_param < 2:
            return False
        for idx_var in range(2, num_param):
            if num_param % idx_var == 0:
                return False
        return True

    first_val: int = 2
    while first_val <= 100:
        if not is_prime(first_val):
            first_val += 1
            continue

        second_val: int = 2
        while second_val <= 100:
            if not is_prime(second_val):
                second_val += 1
                continue

            third_val: int = 2
            while third_val <= 100:
                if not is_prime(third_val):
                    third_val += 1
                    continue

                product_val: int = first_val * second_val * third_val
                if product_val == a_param:
                    return True

                third_val += 1
            second_val += 1
        first_val += 1

    return False