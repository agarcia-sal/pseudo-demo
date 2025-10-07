from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        v = 2
        while v < p - 1:
            if p % v == 0:
                return False
            v += 1
        return True

    found_flag = False
    outer_counter = 2
    while outer_counter <= 0x64 and not found_flag:
        if is_prime(outer_counter):
            middle_counter = 2
            while middle_counter <= 100 and not found_flag:
                if is_prime(middle_counter):
                    inner_counter = 2
                    while inner_counter <= 100 and not found_flag:
                        if is_prime(inner_counter):
                            product_val = outer_counter * middle_counter * inner_counter
                            if product_val == x:
                                found_flag = True
                        inner_counter += 1
                middle_counter += 1
        outer_counter += 1
    return found_flag