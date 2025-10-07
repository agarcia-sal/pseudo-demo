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
    split_list = numbers.split(' ')
    filtered_list = [num for num in split_list if num != '']
    sorted_list = filtered_list[:]
    for i in range(len(sorted_list) - 1):
        for j in range(i + 1, len(sorted_list)):
            if value_map[sorted_list[i]] > value_map[sorted_list[j]]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    result_string = ''
    for k in range(len(sorted_list)):
        if k == 0:
            result_string = sorted_list[k]
        else:
            result_string += ' ' + sorted_list[k]
    return result_string