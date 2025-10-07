def sort_numbers(numbers: str) -> str:
    value_map = {
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
    split_numbers = numbers.split(' ')
    filtered_numbers = [number_word for number_word in split_numbers if number_word]
    sorted_numbers = sorted(filtered_numbers, key=lambda number_word: value_map[number_word])
    return ' '.join(sorted_numbers)