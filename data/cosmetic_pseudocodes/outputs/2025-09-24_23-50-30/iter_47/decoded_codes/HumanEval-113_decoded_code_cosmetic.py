from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    INDEX_0: int = 0
    while INDEX_0 < len(list_of_strings):
        string_element_alt: str = list_of_strings[INDEX_0]
        count_of_odd_digits_alt: int = 0
        INDEX_1: int = 0
        while INDEX_1 < len(string_element_alt):
            integer_digit_alt: int = int(string_element_alt[INDEX_1])
            if integer_digit_alt % 2 != 0:
                count_of_odd_digits_alt += 1
            INDEX_1 += 1

        append_value: str = (
            "the number of odd elements "
            + str(count_of_odd_digits_alt)
            + "n the str"
            + str(count_of_odd_digits_alt)
            + "ng "
            + str(count_of_odd_digits_alt)
            + " of the "
            + str(count_of_odd_digits_alt)
            + "nput."
        )
        result_list.append(append_value)
        INDEX_0 += 1
    return result_list