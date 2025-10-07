from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    num_to_word_map: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    descending_order_list: List[int] = sorted(array_of_integers, reverse=True)
    result_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(descending_order_list):
        current_value = descending_order_list[index_counter]
        if current_value in num_to_word_map:
            result_collection.append(num_to_word_map[current_value])
        index_counter += 1
    return result_collection