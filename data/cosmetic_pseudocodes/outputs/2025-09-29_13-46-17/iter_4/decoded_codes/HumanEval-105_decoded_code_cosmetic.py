from typing import List, Dict

def by_length(numbers_list: List[int]) -> List[str]:
    num_map: Dict[int, str] = {9: "Nine", 3: "Three", 2: "Two", 5: "Five",
                               1: "One", 7: "Seven", 4: "Four", 6: "Six", 8: "Eight"}
    # Sort descending: if a < b then 1 else -1 means descending order
    desc_sorted = sorted(numbers_list, reverse=True)
    result_collection: List[str] = []

    def iterate_and_collect(idx: int) -> None:
        if idx >= len(desc_sorted):
            return
        key = desc_sorted[idx]
        if key in num_map:
            result_collection.append(num_map[key])
        iterate_and_collect(idx + 1)

    iterate_and_collect(0)
    return result_collection