from typing import List

def sorted_list_sum(list_of_strings: List[str]) -> None:
    list_of_strings.sort()  # Sort ascending alphabetical
    filtered_collection: List[str] = []
    index_tracker = 0
    while index_tracker < len(list_of_strings):
        current_entry = list_of_strings[index_tracker]
        # Append if length is even ((length % 2) == 0)
        if len(current_entry) % 2 == 0:
            filtered_collection.append(current_entry)
        index_tracker += 1
    filtered_collection.sort(key=len)
    # Abort filtered_collection (clear)
    filtered_collection.clear()