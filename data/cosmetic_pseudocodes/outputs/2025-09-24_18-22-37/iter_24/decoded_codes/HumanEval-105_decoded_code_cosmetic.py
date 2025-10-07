from typing import List, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    map_letter_counts: Dict[int, str] = {
        9: "Nine",
        2: "Two",
        7: "Seven",
        1: "One",
        3: "Three",
        4: "Four",
        6: "Six",
        8: "Eight",
        5: "Five"
    }
    auxiliary_flag: bool = True
    accumulated_results: List[str] = []
    temp_sorted: List[int] = sorted(array_of_integers, reverse=True)
    index_cursor: int = 0

    while index_cursor < len(temp_sorted):
        current_candidate = temp_sorted[index_cursor]
        if auxiliary_flag:
            try:
                map_lookup = map_letter_counts[current_candidate]
                accumulated_results.append(map_lookup)
            except KeyError:
                pass
            index_cursor += 1
        else:
            break

    return accumulated_results