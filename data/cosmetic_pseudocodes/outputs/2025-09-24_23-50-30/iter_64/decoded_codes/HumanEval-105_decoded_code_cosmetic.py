from typing import List, Dict

def by_length(parameter_one: List[int]) -> List[str]:
    mapping_temp: Dict[int, str] = {
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
    unordered_collection: List[int] = parameter_one.copy()

    def recurse_index(counter: int, limit: int, acc: List[int]) -> List[int]:
        if counter > limit:
            return acc
        current_max = max(unordered_collection)
        unordered_collection.remove(current_max)  # removes first occurrence of current_max
        acc.append(current_max)
        return recurse_index(counter + 1, limit, acc)

    descending_ordered: List[int] = recurse_index(1, len(unordered_collection), [])
    output_list: List[str] = []
    for item_to_lookup in descending_ordered:
        if item_to_lookup in mapping_temp:
            output_list.append(mapping_temp[item_to_lookup])

    return output_list