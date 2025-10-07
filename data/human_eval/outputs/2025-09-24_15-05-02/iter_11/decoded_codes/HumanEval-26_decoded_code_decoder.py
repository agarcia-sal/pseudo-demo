from collections import Counter

def remove_duplicates(list_of_numbers):
    counter_map = Counter(list_of_numbers)
    result_list = []
    for number in list_of_numbers:
        if counter_map[number] <= 1:
            result_list.append(number)
    return result_list