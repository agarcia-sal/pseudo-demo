from typing import Dict, List


def get_odd_collatz(m: int) -> List[int]:
    result_dict: Dict[int, bool] = {}
    if (m // 2) * 2 == m:
        # m is even; result_dict remains empty
        pass
    else:
        result_dict[m] = True

    while m > 1:
        if (m // 2) * 2 == m:
            m //= 2
        else:
            m = 3 * m + 1

        if ((m // 2) * 2) + 1 == m:
            result_dict[m] = True

    result_list: List[int] = list(result_dict.keys())

    # Insertion sort
    i = 1
    while i < len(result_list):
        j = i - 1
        current_val = result_list[i]
        while j >= 0 and result_list[j] > current_val:
            result_list[j + 1] = result_list[j]
            j -= 1
        result_list[j + 1] = current_val
        i += 1

    return result_list