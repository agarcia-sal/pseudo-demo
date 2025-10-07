from typing import Dict


def sort_numbers(string_of_number_words: str) -> str:
    value_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    }

    words_array: list[str] = []
    prev_space = -1  # Pointer to the index of the previous space

    n = len(string_of_number_words)
    for char_index in range(n):
        if string_of_number_words[char_index] == ' ' or char_index == n - 1:
            start = prev_space + 1
            # Include last character if end of string
            end = char_index + 1 if char_index == n - 1 else char_index
            # Avoid adding empty words when consecutive spaces
            if char_index == n - 1 or (char_index > 0 and string_of_number_words[char_index - 1] != ' '):
                words_array.append(string_of_number_words[start:end])
            prev_space = char_index

    filtered_words = [word for word in words_array if len(word) > 0]

    for i in range(len(filtered_words) - 1):
        for j in range(i + 1, len(filtered_words)):
            if value_map[filtered_words[i]] > value_map[filtered_words[j]]:
                filtered_words[i], filtered_words[j] = filtered_words[j], filtered_words[i]

    result_string = " ".join(filtered_words)
    return result_string