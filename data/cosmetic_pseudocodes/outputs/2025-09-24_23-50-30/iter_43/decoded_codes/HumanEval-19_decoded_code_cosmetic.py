from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    number_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    filtered_words: List[str] = []
    index: int = 0
    split_words: List[str] = string_of_number_words.split(" ")
    while index < len(split_words):
        if split_words[index] != "":
            filtered_words.append(split_words[index])
        index += 1

    # Bubble sort by numeric value from number_map
    for i in range(len(filtered_words) - 1):
        for j in range(len(filtered_words) - 1 - i):
            if number_map[filtered_words[j]] > number_map[filtered_words[j + 1]]:
                filtered_words[j], filtered_words[j + 1] = filtered_words[j + 1], filtered_words[j]

    result: str = ""
    pos: int = 0
    while pos < len(filtered_words):
        if pos == 0:
            result = filtered_words[pos]
        else:
            result += " " + filtered_words[pos]
        pos += 1

    return result