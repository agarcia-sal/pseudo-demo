from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    result_list: List[int] = [1, 3]
    index_counter: int = 2

    while index_counter <= integer_n:
        if (index_counter - 2 * (index_counter // 2)) == 0:
            # index_counter is even
            result_list.append((index_counter // 2) + 1)
        else:
            # index_counter is odd
            result_list.append(result_list[index_counter - 2] + result_list[index_counter - 3] + ((index_counter + 3) // 2))
        index_counter += 1

    return result_list