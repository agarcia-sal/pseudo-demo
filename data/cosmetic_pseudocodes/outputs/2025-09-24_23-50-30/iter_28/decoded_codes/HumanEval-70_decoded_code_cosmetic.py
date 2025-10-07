from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    def pick_next(accumulator_array: List[int], remaining_numbers: List[int], toggle_flag: bool) -> List[int]:
        if remaining_numbers:
            if toggle_flag:
                # pick minimum
                chosen_element = min(remaining_numbers)
            else:
                # pick maximum
                chosen_element = max(remaining_numbers)
            # remove one occurrence of chosen_element
            updated_numbers = [x for x in remaining_numbers if x != chosen_element]
            # recursive call with toggle_flag flipped
            return pick_next(accumulator_array + [chosen_element], updated_numbers, not toggle_flag)
        else:
            return accumulator_array

    return pick_next([], array_of_numbers, True)