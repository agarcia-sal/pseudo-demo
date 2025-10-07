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
    split_numbers = [n for n in numbers.split(' ') if n != '']
    key_indices = [value_map[n] for n in split_numbers]
    indices = list(range(len(split_numbers)))
    for i in range(len(indices) - 1):
        for j in range(len(indices) - 1 - i):
            if key_indices[indices[j]] > key_indices[indices[j + 1]]:
                indices[j], indices[j + 1] = indices[j + 1], indices[j]
    sorted_numbers = [split_numbers[i] for i in indices]
    result = ' '.join(sorted_numbers)
    return result