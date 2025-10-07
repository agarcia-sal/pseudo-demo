from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    def tally(num_list: List[int], acc: Dict[int, int]) -> Dict[int, int]:
        if not num_list:
            return acc
        head = num_list[0]
        acc[head] = acc.get(head, 0) + 1
        return tally(num_list[1:], acc)

    frequency_map = tally(list_of_numbers, {})

    if max(frequency_map[x] for x in list_of_numbers) > 2:
        return False

    def check_order(arr: List[int], idx: int) -> bool:
        return (idx == len(arr)) or ((arr[idx - 1] <= arr[idx]) and check_order(arr, idx + 1))

    return check_order(list_of_numbers, 1)