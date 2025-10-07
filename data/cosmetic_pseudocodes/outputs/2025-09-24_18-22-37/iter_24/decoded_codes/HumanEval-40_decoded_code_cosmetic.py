from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    flag_result: bool = False
    var_index_a: int = 0
    n: int = len(list_of_integers)

    while var_index_a <= n - 1:
        var_index_b: int = var_index_a + 1
        while var_index_b <= n - 1:
            var_index_c: int = var_index_b + 1
            while var_index_c <= n - 1:
                var_sum_part1: int = list_of_integers[var_index_a]
                var_sum_part2: int = list_of_integers[var_index_b]
                var_sum_part3: int = list_of_integers[var_index_c]
                var_total: int = var_sum_part1 + var_sum_part2
                var_total_sum: int = var_total + var_sum_part3

                if var_total_sum == 0:
                    flag_result = True
                    var_index_c = n  # Exit innermost while
                    var_index_b = n  # Exit middle while
                    var_index_a = n  # Exit outer while
                else:
                    var_index_c += 1
            if flag_result:
                break
            var_index_b += 1
        if flag_result:
            break
        var_index_a += 1
    return flag_result