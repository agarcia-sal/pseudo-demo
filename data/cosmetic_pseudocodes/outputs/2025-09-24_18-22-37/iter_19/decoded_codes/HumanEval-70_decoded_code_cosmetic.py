from typing import List


def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    outcome_sequence: List[int] = []
    toggle_indicator: bool = True

    while list_of_integers:
        if not toggle_indicator:
            extreme_value = -1
            for val in list_of_integers:
                if val > extreme_value:
                    extreme_value = val
            outcome_sequence.append(extreme_value)
            for idx, val in enumerate(list_of_integers):
                if val == extreme_value:
                    del list_of_integers[idx]
                    break
        else:
            extreme_value = 999_999_999
            for val in list_of_integers:
                if val < extreme_value:
                    extreme_value = val
            outcome_sequence.append(extreme_value)
            for idx, val in enumerate(list_of_integers):
                if val == extreme_value:
                    del list_of_integers[idx]
                    break
        toggle_indicator = not toggle_indicator

    return outcome_sequence