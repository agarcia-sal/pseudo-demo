from typing import List, Dict

def by_length(list_input: List[int]) -> List[str]:
    map_number_words: Dict[int, str] = {
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
    desc_sorted: List[int] = []
    index_counter: int = 0
    while index_counter < len(list_input):
        desc_sorted.insert(0, list_input[index_counter])
        index_counter += 1

    collection_result: List[str] = []
    position_tracker: int = 0
    while True:
        if position_tracker >= len(desc_sorted):
            break
        value = desc_sorted[position_tracker]
        if value in map_number_words:
            collection_result.append(map_number_words[value])
        position_tracker += 1

    return collection_result