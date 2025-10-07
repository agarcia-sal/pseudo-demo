from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n <= 0:
        return [1]

    list_result: List[int] = [1, 3]
    index_counter = 2
    while index_counter <= integer_n:
        if index_counter % 2 == 0:
            list_result.append((index_counter // 2) + 1)
        else:
            # index_counter - 1 and index_counter - 2 are valid indices here
            list_result.append(
                list_result[index_counter - 1]
                + list_result[index_counter - 2]
                + ((index_counter + 3) // 2)
            )
        index_counter += 1

    return list_result