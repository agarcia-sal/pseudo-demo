from typing import List

def tri(integer_n: int) -> List[int]:
    def recurse(acc_list: List[int], index: int, limit: int) -> List[int]:
        if index > limit:
            return acc_list
        if (index % 2) == 0:
            acc_list = acc_list + [(index // 2) + 1]
        else:
            val1 = acc_list[index - 1]
            val2 = acc_list[index - 2]
            val3 = (index + 3) // 2
            acc_list = acc_list + [val1 + val2 + val3]
        return recurse(acc_list, index + 1, limit)

    if not (integer_n > 0):
        return [1]
    return recurse([1, 3], 2, integer_n)