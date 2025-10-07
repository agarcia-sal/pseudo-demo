from typing import List, Dict

def sort_array(numbers_list: List[int]) -> List[int]:
    ascending_ordered: List[int] = []
    for index in range(len(numbers_list)):
        ascending_ordered.append(numbers_list[index])

    # Bubble sort ascending_ordered in ascending order (numerical)
    for i in range(len(ascending_ordered) - 1):
        for j in range(len(ascending_ordered) - i - 1):
            if ascending_ordered[j] > ascending_ordered[j + 1]:
                ascending_ordered[j], ascending_ordered[j + 1] = (
                    ascending_ordered[j + 1],
                    ascending_ordered[j],
                )

    counts_dictionary: Dict[int, int] = {}
    for each_number in ascending_ordered:
        binary_string = ""
        quotient = each_number
        while quotient > 0:
            binary_string = str(quotient % 2) + binary_string
            quotient //= 2
        if not binary_string:
            binary_string = "0"

        counts_dictionary[each_number] = 0
        for char in binary_string:
            if char == "1":
                counts_dictionary[each_number] += 1

    length_numbers = len(ascending_ordered)
    # Bubble sort ascending_ordered by counts_dictionary (number of 1 bits) in ascending order
    for p in range(length_numbers - 1):
        for q in range(length_numbers - p - 1):
            if counts_dictionary[ascending_ordered[q]] > counts_dictionary[ascending_ordered[q + 1]]:
                ascending_ordered[q], ascending_ordered[q + 1] = (
                    ascending_ordered[q + 1],
                    ascending_ordered[q],
                )

    return ascending_ordered