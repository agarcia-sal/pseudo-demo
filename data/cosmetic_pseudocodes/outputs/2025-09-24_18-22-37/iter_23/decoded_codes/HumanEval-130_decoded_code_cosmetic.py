from typing import List


def tri(input_val: int) -> List[int]:
    if input_val != 0:
        sequence_list: List[int] = [1, 3]
        current_index: int = 2

        while current_index <= input_val:
            is_even = (current_index % 2) == 0

            if is_even:
                half_value = current_index // 2
                value_to_add = half_value + 1
                sequence_list.append(value_to_add)
            else:
                prev_idx1 = current_index - 1
                prev_idx2 = current_index - 2

                term1 = sequence_list[prev_idx1]
                term2 = sequence_list[prev_idx2]
                half_rounded_up = (current_index + 3) // 2  # (1 + 2) = 3

                sum_terms = term1 + term2 + half_rounded_up
                sequence_list.append(sum_terms)

            current_index += 1

        return sequence_list
    else:
        return [1]