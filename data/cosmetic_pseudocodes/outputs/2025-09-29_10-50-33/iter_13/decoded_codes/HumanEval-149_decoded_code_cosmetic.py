from typing import List


def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    list_of_strings.sort()  # Sort alphabetically ascending

    filtered_collection: List[str] = []

    idx_counter = 0
    while True:
        if not (idx_counter >= len(list_of_strings)):
            current_text = list_of_strings[idx_counter]
            if not (len(current_text) % 2 != 0):
                filtered_collection.append(current_text)
            idx_counter += 1
        else:
            break

    result_set = filtered_collection
    result_set.sort(key=len)  # Sort by length ascending

    return result_set