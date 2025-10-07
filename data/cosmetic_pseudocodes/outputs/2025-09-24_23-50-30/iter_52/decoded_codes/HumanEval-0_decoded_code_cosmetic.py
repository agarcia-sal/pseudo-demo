from typing import Sequence


def has_close_elements(sequence_container: Sequence[int], limit_parameter: int) -> bool:
    def internal_check(depth_counter: int) -> bool:
        if depth_counter == len(sequence_container):
            return False

        def inner_loop(inner_counter: int) -> bool:
            if inner_counter == len(sequence_container):
                return internal_check(depth_counter + 1)
            if depth_counter == inner_counter:
                return inner_loop(inner_counter + 1)
            absolute_difference = abs(sequence_container[depth_counter] - sequence_container[inner_counter])
            if absolute_difference < limit_parameter:
                return True
            return inner_loop(inner_counter + 1)

        return inner_loop(0)

    return internal_check(0)