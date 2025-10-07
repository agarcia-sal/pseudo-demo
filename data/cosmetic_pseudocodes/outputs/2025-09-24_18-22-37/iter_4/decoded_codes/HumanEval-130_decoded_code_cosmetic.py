from typing import List


def tri(integer_n: int) -> List[int]:
    result_list: List[int] = []
    if integer_n == 0:
        result_list = [1]
        return result_list

    result_list = [1, 3]
    counter: int = 2

    while counter <= integer_n:
        if counter % 2 == 0:
            value = (counter // 2) + 1
            result_list.append(value)
        else:
            val1 = result_list[counter - 1]
            val2 = result_list[counter - 2]
            val3 = ((counter + 3) // 2)
            value = val1 + val2 + val3
            result_list.append(value)
        counter += 1

    return result_list