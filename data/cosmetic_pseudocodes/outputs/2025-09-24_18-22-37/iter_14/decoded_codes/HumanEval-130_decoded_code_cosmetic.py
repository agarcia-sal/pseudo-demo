from typing import List

def tri(param_a: int) -> List[int]:
    if param_a <= 0:
        return [1]

    result_list: List[int] = [1, 3]
    counter: int = 2

    while counter <= param_a:
        mod_result: int = counter % 2

        if mod_result == 0:
            half_plus_one: int = (counter // 2) + 1
            result_list.append(half_plus_one)
        else:
            val1: int = result_list[counter - 1]
            val2: int = result_list[counter - 2]
            half_plus_two: int = (counter + 3) // 2
            result_list.append(val1 + val2 + half_plus_two)

        counter += 1

    return result_list