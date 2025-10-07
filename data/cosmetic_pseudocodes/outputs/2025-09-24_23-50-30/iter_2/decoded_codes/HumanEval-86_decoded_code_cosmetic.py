from collections import deque
from typing import List

def anti_shuffle(input_string: str) -> str:
    words_queue: deque[str] = deque(input_string.split(' '))
    sorted_words_stack: List[str] = []

    while words_queue:
        current_word: str = words_queue.popleft()
        chars_array: List[str] = list(current_word)
        chars_array.sort(reverse=True)
        # Reverse chars_array to get ascending order as per pseudocode
        chars_array.reverse()
        sorted_word = ''.join(chars_array[i] for i in range(len(chars_array) - 1, -1, -1))
        sorted_words_stack.append(sorted_word)

    result_words_list: List[str] = []
    while sorted_words_stack:
        result_words_list.insert(0, sorted_words_stack.pop())

    result_string = ''
    for index in range(len(result_words_list)):
        result_string += result_words_list[index]
        if index < len(result_words_list) - 1:
            result_string += ' '

    return result_string