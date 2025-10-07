from typing import Dict


def sort_numbers(string_of_number_words: str) -> str:
    map_values: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    chunks = string_of_number_words.split(" ")
    filtered_words = []
    idx = 0
    while idx < len(chunks):
        current_word = chunks[idx]
        if current_word != "":
            filtered_words.append(current_word)
        idx += 1
    n = len(filtered_words)
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            val_i = map_values[filtered_words[i]]
            val_j = map_values[filtered_words[j]]
            if val_i > val_j:
                filtered_words[i], filtered_words[j] = filtered_words[j], filtered_words[i]
            j += 1
        i += 1
    joined_result = ""
    k = 0
    while k < n:
        joined_result += filtered_words[k]
        if k < n - 1:
            joined_result += " "
        k += 1
    return joined_result