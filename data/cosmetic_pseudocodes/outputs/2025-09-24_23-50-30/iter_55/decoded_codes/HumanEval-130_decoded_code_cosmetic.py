from typing import List


def tri(recursive_p: int) -> List[int]:
    if recursive_p == 0:
        return [1]
    else:
        result_list: List[int] = [1, 3]

        def loop(index: int, acc: List[int]) -> List[int]:
            if index <= recursive_p:
                is_even = (index % 2) == 0
                if is_even:
                    result_to_add = index // 2 + 1
                else:
                    result_to_add = acc[index - 1] + acc[index - 2] + ((index + 3) // 2)
                acc.append(result_to_add)
                return loop(index + 1, acc)
            else:
                return acc

        return loop(2, result_list)