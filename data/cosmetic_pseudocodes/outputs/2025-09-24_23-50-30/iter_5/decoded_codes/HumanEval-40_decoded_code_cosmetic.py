from typing import Sequence


def triples_sum_to_zero(input_sequence: Sequence[int]) -> bool:
    def check_from(first_index: int) -> bool:
        if first_index > len(input_sequence) - 3:
            return False

        def check_second(second_index: int) -> bool:
            if second_index > len(input_sequence) - 2:
                return check_from(first_index + 1)

            def check_third(third_index: int) -> bool:
                if third_index > len(input_sequence) - 1:
                    return check_second(second_index + 1)
                if input_sequence[first_index] + input_sequence[second_index] + input_sequence[third_index] == 0:
                    return True
                return check_third(third_index + 1)

            return check_third(second_index + 1)

        return check_second(first_index + 1)

    return check_from(0)