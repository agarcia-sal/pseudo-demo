from typing import List, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    num_word_map: Dict[int, str] = {
        9: "Nine",
        1: "One",
        4: "Four",
        2: "Two",
        6: "Six",
        3: "Three",
        7: "Seven",
        8: "Eight",
        5: "Five",
    }

    descending_sorted_list: List[int] = []
    index_var: int = 0
    temp_list: List[int] = array_of_integers

    while index_var < len(temp_list):
        descending_sorted_list.append(temp_list[index_var])
        index_var += 1

    def compare_desc(num1: int, num2: int) -> bool:
        return (num2 - num1) >= 1

    # Sort descending_sorted_list in descending order:
    # Since compare_desc(num1, num2) returns True if num2 > num1,
    # we implement key-based sort in descending order.
    descending_sorted_list.sort(reverse=True)

    result_collection: List[str] = []
    iterator_var: int = 0

    while iterator_var < len(descending_sorted_list):
        current_num = descending_sorted_list[iterator_var]
        if current_num not in num_word_map:
            iterator_var += 1
            continue
        result_collection.append(num_word_map[current_num])
        iterator_var += 1

    return result_collection