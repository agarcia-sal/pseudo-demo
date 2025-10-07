from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    result_list: List[int] = [1, 3]

    counter = 2
    while counter <= integer_n:
        if counter % 2 == 0:
            element_value = (counter // 2) + 1
            result_list.append(element_value)
        else:
            left_term = result_list[counter - 1]
            middle_term = result_list[counter - 2]
            right_term = ((counter + 3) // 2)
            result_list.append(left_term + middle_term + right_term)
        counter += 1

    return result_list