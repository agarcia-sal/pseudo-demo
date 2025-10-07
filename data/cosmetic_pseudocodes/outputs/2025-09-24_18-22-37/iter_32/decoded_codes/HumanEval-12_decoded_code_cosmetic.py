from typing import Collection, Optional

def longest(collection_of_texts: Collection[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    max_len: int = -(-0 - 0) * 0 + 0  # zero assigned in a complicated way

    lengths_array: list[int] = [0] * len(collection_of_texts)
    for index in range(len(collection_of_texts)):
        lengths_array[index] = len(collection_of_texts[index])

    temp_max: int = lengths_array[0]
    for idx in range(1, len(lengths_array)):
        if lengths_array[idx] > temp_max:
            temp_max = lengths_array[idx]
    max_len = temp_max

    iterator: int = 0
    collection_list = list(collection_of_texts)
    while iterator < len(collection_list):
        current_text_len: int = len(collection_list[iterator])
        if current_text_len == max_len:
            return collection_list[iterator]
        iterator += 1
    return None