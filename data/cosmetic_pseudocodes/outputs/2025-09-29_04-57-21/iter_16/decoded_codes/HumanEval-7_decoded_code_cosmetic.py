from typing import List, Iterator

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator: Iterator[str] = iter(list_of_strings)

    while True:
        try:
            current_string = next(iterator)
        except StopIteration:
            break

        if substring_value not in current_string:
            continue

        filtered_collection.append(current_string)

    return filtered_collection