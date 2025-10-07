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
    split_numbers = []
    i = 0
    while i < len(numbers):
        current_word = ""
        while i < len(numbers) and numbers[i] != ' ':
            current_word += numbers[i]
            i += 1
        if current_word != "":
            split_numbers.append(current_word)
        if i < len(numbers) and numbers[i] == ' ':
            i += 1
    filtered_numbers = []
    j = 0
    while j < len(split_numbers):
        if split_numbers[j] != "":
            filtered_numbers.append(split_numbers[j])
        j += 1
    def compare_by_value_map(x: str, y: str) -> bool:
        if value_map[x] < value_map[y]:
            return True
        else:
            return False
    sorted_numbers = []
    while len(filtered_numbers) > 0:
        min_index = 0
        k = 1
        while k < len(filtered_numbers):
            if value_map[filtered_numbers[k]] < value_map[filtered_numbers[min_index]]:
                min_index = k
            k += 1
        sorted_numbers.append(filtered_numbers[min_index])
        filtered_numbers.pop(min_index)
    result = ""
    m = 0
    while m < len(sorted_numbers):
        if m > 0:
            result += " "
        result += sorted_numbers[m]
        m += 1
    return result