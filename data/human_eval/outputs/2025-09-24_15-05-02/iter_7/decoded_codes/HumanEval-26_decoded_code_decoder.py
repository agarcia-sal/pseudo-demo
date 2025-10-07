from collections import Counter

def remove_duplicates(list_of_numbers):
    element_counts = Counter(list_of_numbers)
    result_list = []
    for element in list_of_numbers:
        if element_counts[element] <= 1:
            result_list.append(element)
    return result_list