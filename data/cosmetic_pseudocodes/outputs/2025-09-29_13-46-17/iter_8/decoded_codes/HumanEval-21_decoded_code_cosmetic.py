from typing import List, Tuple


def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    def aux_recurse(
        remaining_collection: List[float], min_val: float, max_val: float, acc: List[float]
    ) -> List[float]:
        if not remaining_collection:
            return acc[::-1]  # reverse accumulated list
        current_element = remaining_collection[0]
        # Normalize current element to [0,1] range
        normalized = (current_element - min_val) / (max_val - min_val) if max_val != min_val else 0.0
        return aux_recurse(remaining_collection[1:], min_val, max_val, [normalized] + acc)

    def find_minmax(
        data: List[float], current_min: float, current_max: float
    ) -> Tuple[float, float]:
        if not data:
            return current_min, current_max
        hd = data[0]
        new_min = hd if hd < current_min else current_min
        new_max = hd if hd > current_max else current_max
        return find_minmax(data[1:], new_min, new_max)

    if not list_of_numbers:
        return []  # empty input yields empty output

    min_raw, max_raw = find_minmax(list_of_numbers, list_of_numbers[0], list_of_numbers[0])
    return aux_recurse(list_of_numbers, min_raw, max_raw, [])