from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    beta_list: List[int] = [1, 3]
    counter: int = 2

    while counter <= integer_n:
        remainder = counter % 2
        if remainder == 0:
            quotient = counter // 2
            value_to_append = quotient + 1
            beta_list.append(value_to_append)
        else:
            first_index = counter - 1
            second_index = counter - 2
            sum_indices = beta_list[first_index] + beta_list[second_index]
            adjustment = (counter + 3) // 2
            total_value = sum_indices + adjustment
            beta_list.append(total_value)
        counter += 1

    return beta_list