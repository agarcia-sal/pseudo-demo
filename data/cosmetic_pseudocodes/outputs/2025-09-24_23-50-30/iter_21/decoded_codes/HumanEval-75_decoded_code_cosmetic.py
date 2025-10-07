from typing import List


def is_multiply_prime(a_param: int) -> bool:
    def check_prime(value: int) -> bool:
        if value < 2:
            return False
        for candidate in range(2, value):
            if value % candidate == 0:
                return False
        return True

    prime_i_list: List[int] = [num for num in range(2, 101) if check_prime(num)]
    prime_j_list: List[int] = [num for num in range(2, 101) if check_prime(num)]
    prime_k_list: List[int] = [num for num in range(2, 101) if check_prime(num)]

    found_flag: bool = False
    idx_i: int = 0
    while idx_i < len(prime_i_list) and not found_flag:
        current_i: int = prime_i_list[idx_i]
        idx_j: int = 0
        while idx_j < len(prime_j_list) and not found_flag:
            current_j: int = prime_j_list[idx_j]
            idx_k: int = 0
            while idx_k < len(prime_k_list) and not found_flag:
                current_k: int = prime_k_list[idx_k]
                if current_i * current_j * current_k == a_param:
                    found_flag = True
                idx_k += 1
            idx_j += 1
        idx_i += 1

    return found_flag