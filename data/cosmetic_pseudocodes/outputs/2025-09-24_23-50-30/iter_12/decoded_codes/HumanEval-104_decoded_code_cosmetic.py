from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def recursive_filter(idx: int, collected: List[int]) -> List[int]:
        if idx >= len(list_of_positive_integers):
            return collected
        current_val = list_of_positive_integers[idx]
        digits = str(current_val)
        # Check if all digits are odd
        is_all_odd = all((int(d) % 2) == 1 for d in digits)
        if is_all_odd:
            return recursive_filter(idx + 1, collected + [current_val])
        else:
            return recursive_filter(idx + 1, collected)

    filtered_results = recursive_filter(0, [])
    sorted_results: List[int] = []
    while filtered_results:
        min_val = filtered_results[0]
        for val in filtered_results:
            if val < min_val:
                min_val = val
        sorted_results.append(min_val)
        filtered_results.remove(min_val)
    return sorted_results