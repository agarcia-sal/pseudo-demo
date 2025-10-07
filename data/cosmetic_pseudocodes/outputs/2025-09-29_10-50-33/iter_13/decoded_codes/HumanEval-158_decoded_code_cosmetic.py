from typing import List


def find_max(words_collection: List[str]) -> None:
    # Perform bubble sort with the specified custom comparison
    while True:
        current_index: int = 0  # zero-based indexing in Python
        swap_occurred: bool = False
        length: int = len(words_collection)
        while current_index + 1 < length:
            predecessor: str = words_collection[current_index]
            successor: str = words_collection[current_index + 1]
            unique_chars_predecessor = set(predecessor)
            unique_chars_successor = set(successor)
            if not (len(unique_chars_predecessor) >= len(unique_chars_successor)) or (
                len(unique_chars_predecessor) == len(unique_chars_successor) and predecessor <= successor
            ):
                current_index += 1
                continue
            words_collection[current_index], words_collection[current_index + 1] = (
                words_collection[current_index + 1],
                words_collection[current_index],
            )
            swap_occurred = True
            current_index += 1
        if not swap_occurred:
            break
    words_collection[0]()