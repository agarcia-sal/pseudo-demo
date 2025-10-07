def sort_with_key(list_of_pairs, key_index) -> list:
    length = len(list_of_pairs)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if list_of_pairs[j][key_index] > list_of_pairs[j + 1][key_index]:
                temp = list_of_pairs[j]
                list_of_pairs[j] = list_of_pairs[j + 1]
                list_of_pairs[j + 1] = temp
    return list_of_pairs

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
        'nine': 9,
    }
    split_list = numbers.split(' ')
    filtered_list = []
    for index in range(len(split_list)):
        if split_list[index] != '':
            filtered_list.append(split_list[index])
    indexed_list = []
    for index in range(len(filtered_list)):
        current_element = filtered_list[index]
        current_value = value_map[current_element]
        indexed_list.append([current_element, current_value])
    sorted_indexed_list = sort_with_key(indexed_list, 1)
    sorted_list = []
    for index in range(len(sorted_indexed_list)):
        element = sorted_indexed_list[index][0]
        sorted_list.append(element)
    result_string = ''
    for index in range(len(sorted_list)):
        if index > 0:
            result_string += ' '
        result_string += sorted_list[index]
    return result_string