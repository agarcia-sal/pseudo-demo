from collections import deque
from functools import reduce
from typing import List


def anti_shuffle(input_string: str) -> str:
    words_queue: deque[str] = deque(input_string.split(" "))
    sorted_collection: List[str] = []
    while words_queue:
        current_word: str = words_queue.popleft()
        chars_array: List[str] = list(current_word)
        chars_array.sort()
        reconstructed_word: str = "".join(chars_array)
        sorted_collection.append(reconstructed_word)
    final_output: str = reduce(lambda acc, val: acc + " " + val, sorted_collection, "")
    return final_output.strip()