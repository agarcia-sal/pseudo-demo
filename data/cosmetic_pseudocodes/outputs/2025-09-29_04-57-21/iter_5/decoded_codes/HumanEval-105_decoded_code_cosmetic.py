from typing import List, Dict

def by_length(arr: List[int]) -> List[str]:
    dict_map: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    result_list: List[str] = []

    def process_items(index: int) -> None:
        if not (index < len(arr)):
            return
        sorted_version = sorted(arr, reverse=True)
        current_val = sorted_version[index]
        if current_val in dict_map:
            result_list.append(dict_map[current_val])
        process_items(index + 1)

    process_items(0)

    return result_list