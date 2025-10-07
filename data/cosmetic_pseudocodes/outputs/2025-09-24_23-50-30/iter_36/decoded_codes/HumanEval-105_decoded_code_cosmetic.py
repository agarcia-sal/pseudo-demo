from typing import List, Sequence

def by_length(input_sequence: Sequence[int]) -> List[str]:
    numeral_map: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }

    def accumulate_labels(index: int, source_list: Sequence[int], collector: List[str]) -> None:
        if index >= len(source_list):
            return
        candidate = source_list[index]
        if candidate in numeral_map:
            collector.append(numeral_map[candidate])
        accumulate_labels(index + 1, source_list, collector)

    temp_sorted = sorted(input_sequence, reverse=True)
    result_list: List[str] = []
    accumulate_labels(0, temp_sorted, result_list)
    return result_list