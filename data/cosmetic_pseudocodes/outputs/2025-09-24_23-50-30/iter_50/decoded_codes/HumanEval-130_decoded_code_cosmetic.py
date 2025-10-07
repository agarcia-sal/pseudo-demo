from typing import List


def tri(integer_n: int) -> List[int]:
    def recurse(accum_list: List[int], current_index: int, limit: int) -> List[int]:
        if current_index > limit:
            return accum_list

        evenness: bool = (current_index % 2 == 0)
        if evenness:
            updated_list = accum_list + [(current_index // 2) + 1]
        else:
            val1 = accum_list[current_index - 1]
            val2 = accum_list[current_index - 2]
            val3 = (current_index + 3) // 2
            updated_list = accum_list + [val1 + val2 + val3]

        return recurse(updated_list, current_index + 1, limit)

    if integer_n == 0:
        return [1]
    return recurse([1, 3], 2, integer_n)