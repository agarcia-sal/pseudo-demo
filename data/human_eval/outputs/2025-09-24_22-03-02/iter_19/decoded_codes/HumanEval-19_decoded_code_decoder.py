from typing import Dict

def sort_numbers(numbers: str) -> str:
    value_map: Dict[str, int] = {
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
    words_list = []
    split_numbers = numbers.split(' ')
    index = 0
    while index < len(split_numbers):
        if split_numbers[index] != '':
            words_list.append(split_numbers[index])
        index += 1
    length_words_list = len(words_list)
    for i in range(length_words_list - 1):
        for j in range(i + 1, length_words_list):
            if value_map[words_list[i]] > value_map[words_list[j]]:
                words_list[i], words_list[j] = words_list[j], words_list[i]
    result = ''
    index = 0
    while index < length_words_list:
        if index == 0:
            result = words_list[index]
        else:
            result += ' ' + words_list[index]
        index += 1
    return result