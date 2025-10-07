from typing import List, Dict, Tuple

def is_prime(parameter_alpha: int) -> bool:
    boolean_beta = False
    integer_gamma = parameter_alpha
    integer_delta = 1

    if not (integer_gamma > integer_delta):
        boolean_beta = False
        return boolean_beta

    integer_delta = 3
    if integer_gamma <= integer_delta:
        return True

    integer_omega = 2

    def divisible(mod_dividend: int, mod_divisor: int) -> bool:
        return (mod_dividend - ((mod_dividend // mod_divisor) * mod_divisor)) == 0

    if divisible(integer_gamma, integer_omega) or divisible(integer_gamma, integer_delta):
        return False

    integer_omega = 5

    def RepeatCheck(counter: int) -> bool:
        if (counter * counter) > integer_gamma:
            return True
        else:
            if divisible(integer_gamma, counter) or divisible(integer_gamma, counter + 2):
                return False
            else:
                return RepeatCheck(counter + 6)

    return RepeatCheck(integer_omega)


class Solution:
    def mostFrequentPrime(self, parameter_mat: List[List[int]]) -> int:
        integer_var_m = 0
        while integer_var_m < len(parameter_mat):
            integer_var_m += 1
        integer_var_m -= 1

        integer_var_n = 0
        while integer_var_n < len(parameter_mat[0]):
            integer_var_n += 1
        integer_var_n -= 1

        LIST_pair_directions: List[Tuple[int, int]] = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

        map_prime_count: Dict[int, int] = {}

        def CheckPrimeInDirection(origin_x: int, origin_y: int, delta_x: int, delta_y: int, num_so_far: int) -> None:
            integer_next_x = origin_x + delta_x
            integer_next_y = origin_y + delta_y
            if 0 <= integer_next_x <= integer_var_m:
                if 0 <= integer_next_y <= integer_var_n:
                    integer_new_num = (num_so_far * 10) + parameter_mat[integer_next_x][integer_next_y]
                    if integer_new_num > 10:
                        if is_prime(integer_new_num):
                            if integer_new_num in map_prime_count:
                                map_prime_count[integer_new_num] += 1
                            else:
                                map_prime_count[integer_new_num] = 1
                    CheckPrimeInDirection(integer_next_x, integer_next_y, delta_x, delta_y, integer_new_num)

        for integer_idx in range(integer_var_m + 1):
            for integer_idy in range(integer_var_n + 1):
                for integer_ux, integer_uy in LIST_pair_directions:
                    CheckPrimeInDirection(integer_idx, integer_idy, integer_ux, integer_uy, parameter_mat[integer_idx][integer_idy])

        if len(map_prime_count) == 0:
            return -1

        integer_candidate_freq = -1
        integer_candidate_value = -1

        for integer_val in map_prime_count.keys():
            if (map_prime_count[integer_val] > integer_candidate_freq) or \
               (map_prime_count[integer_val] == integer_candidate_freq and integer_val > integer_candidate_value):
                integer_candidate_freq = map_prime_count[integer_val]
                integer_candidate_value = integer_val

        return integer_candidate_value