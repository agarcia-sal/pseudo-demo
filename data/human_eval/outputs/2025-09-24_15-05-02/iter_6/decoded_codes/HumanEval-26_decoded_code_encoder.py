import collections

def remove_duplicates(list_of_numbers):
    count_map = collections.Counter(list_of_numbers)
    result_list = []
    for number in list_of_numbers:
        if count_map[number] <= 1:
            result_list.append(number)
    return result_list