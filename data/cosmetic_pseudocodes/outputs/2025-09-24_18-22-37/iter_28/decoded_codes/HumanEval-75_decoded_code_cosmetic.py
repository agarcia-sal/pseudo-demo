from typing import Callable

def is_multiply_prime(alpha: int) -> bool:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False
        for gamma in range(2, beta):
            if beta % gamma == 0:
                return False
        return True

    m = 2
    flag_outer = False
    while m <= 100:
        if_prime_m = is_prime(m)
        if not if_prime_m:
            m += 1
            continue
        n = 2
        while n <= 100:
            if_prime_n = is_prime(n)
            if not if_prime_n:
                n += 1
                continue
            p = 2
            while p <= 100:
                value_prime_p = is_prime(p)
                if not value_prime_p:
                    p += 1
                    continue
                temp_product_1 = m * n
                temp_product_2 = temp_product_1 * p
                if temp_product_2 == alpha:
                    flag_outer = True
                    # break from p loop by setting p to 101
                    p = 101
                else:
                    pass
                p += 1
            if flag_outer:
                n = 101
            else:
                n += 1
        if flag_outer:
            m = 101
        else:
            m += 1
    return flag_outer