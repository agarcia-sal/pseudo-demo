from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(m: int) -> bool:
        def checker(v: int) -> bool:
            if v >= m:
                return True
            if m % v == 0:
                return False
            return checker(v + 1)

        return checker(2)

    found_flag: bool = False
    outer_counter: int = 2
    while outer_counter <= 100 and not found_flag:
        if is_prime(outer_counter):
            middle_counter: int = 2
            while middle_counter <= 100 and not found_flag:
                if is_prime(middle_counter):
                    inner_counter: int = 2
                    while inner_counter <= 100 and not found_flag:
                        if is_prime(inner_counter):
                            if outer_counter * middle_counter * inner_counter == x:
                                found_flag = True
                        inner_counter += 1
                middle_counter += 1
        outer_counter += 1

    return found_flag