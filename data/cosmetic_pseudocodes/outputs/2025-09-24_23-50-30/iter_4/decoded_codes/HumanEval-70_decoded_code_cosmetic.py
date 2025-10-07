from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def recursive_helper(input_list: List[int], flag: bool, acc: List[int]) -> List[int]:
        if not input_list:
            return acc
        chosen_value = min(input_list) if flag else max(input_list)
        seen_chosen = False
        filtered_list = []
        for x in input_list:
            if x == chosen_value and not seen_chosen:
                seen_chosen = True
                continue
            filtered_list.append(x)
        return recursive_helper(filtered_list, not flag, acc + [chosen_value])

    return recursive_helper(list_of_integers, True, [])