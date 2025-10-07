from typing import List


def triples_sum_to_zero(original_list: List[int]) -> bool:
    def recursive_loop_a(counter_a: int) -> bool:
        if counter_a >= len(original_list):
            return False
        def recursive_loop_b(counter_b: int) -> bool:
            if counter_b >= len(original_list):
                return recursive_loop_a(counter_a + 1)
            def recursive_loop_c(counter_c: int) -> bool:
                if counter_c >= len(original_list):
                    return recursive_loop_b(counter_b + 1)
                sum_result = original_list[counter_a] + original_list[counter_b] + original_list[counter_c]
                if sum_result == 0:
                    return True
                return recursive_loop_c(counter_c + 1)
            return recursive_loop_c(counter_b + 1)
        return recursive_loop_b(counter_a + 1)
    return recursive_loop_a(0)