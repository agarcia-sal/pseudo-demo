from typing import List, Dict

def by_length(sequence_of_ints: List[int]) -> List[str]:
    mapping_nums: Dict[int, str] = {
        9: "Nine",
        3: "Three",
        1: "One",
        4: "Four",
        2: "Two",
        6: "Six",
        8: "Eight",
        7: "Seven",
        5: "Five"
    }
    desc_sorted: List[int] = sorted(sequence_of_ints, reverse=True)
    result_collection: List[str] = []

    def process_index(i: int) -> None:
        if i >= len(desc_sorted):
            return
        if desc_sorted[i] in mapping_nums:
            result_collection.append(mapping_nums[desc_sorted[i]])
        process_index(i + 1)

    process_index(0)
    return result_collection