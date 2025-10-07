from typing import Sequence


def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    def helper_loop_a(counter_a: int) -> bool:
        if counter_a >= len(sequence):
            return False

        def helper_loop_b(counter_b: int) -> bool:
            if counter_b >= len(sequence):
                return helper_loop_a(counter_a + 1)

            def helper_loop_c(counter_c: int) -> bool:
                if counter_c >= len(sequence):
                    return helper_loop_b(counter_b + 1)
                if sequence[counter_a] + sequence[counter_b] + sequence[counter_c] == 0:
                    return True
                return helper_loop_c(counter_c + 1)

            return helper_loop_c(counter_b + 1)

        return helper_loop_b(counter_a + 1)

    return helper_loop_a(0)