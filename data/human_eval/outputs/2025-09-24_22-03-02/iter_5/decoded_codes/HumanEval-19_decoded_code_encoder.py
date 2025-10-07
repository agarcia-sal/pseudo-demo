def sort_numbers(numbers):
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
    list_of_words = numbers.split(' ')
    filtered_list = [word for word in list_of_words if word]
    sorted_list = sorted(filtered_list, key=lambda word: value_map[word])
    return ' '.join(sorted_list)