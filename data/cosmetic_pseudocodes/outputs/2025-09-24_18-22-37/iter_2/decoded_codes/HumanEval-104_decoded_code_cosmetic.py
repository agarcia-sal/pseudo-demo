from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_numbers_collection: List[int] = []
    for single_number in list_of_positive_integers:
        digits_string = str(single_number)
        flag_all_odd = True
        for character in digits_string:
            if int(character) % 2 == 0:
                flag_all_odd = False
                break
        if flag_all_odd:
            odd_numbers_collection.append(single_number)
    return sorted(odd_numbers_collection)