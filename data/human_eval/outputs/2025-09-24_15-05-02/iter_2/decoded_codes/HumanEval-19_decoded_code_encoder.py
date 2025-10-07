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
    number_list = [word for word in numbers.split(' ') if word]
    sorted_list = sorted(number_list, key=lambda word: value_map[word])
    result = ' '.join(sorted_list)
    return result