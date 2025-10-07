from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    dictionary_of_numbers: Dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }

    def process_items(arr: List[int], idx: int, result: List[str]) -> List[str]:
        if idx < 0:
            return result
        current = arr[idx]
        if current in dictionary_of_numbers:
            result = result + [dictionary_of_numbers[current]]
        return process_items(arr, idx - 1, result)

    # Sort array descending as per pseudocode comparator b > a
    sorted_array = sorted(array_of_integers, reverse=True)
    return process_items(sorted_array, len(sorted_array) - 1, [])