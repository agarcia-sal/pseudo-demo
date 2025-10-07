from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_dictionary: Dict[str, int] = {}
    list_of_letters: list[str] = []
    maximum_count: int = 0
    index: int = 0

    # Split test_string on spaces using manual parsing as in pseudocode
    while index < len(test_string):
        if test_string[index] == " ":
            list_of_letters.append(test_string[:index])
            test_string = test_string[index + 1 :]
            index = 0
        else:
            index += 1
    if test_string != "":
        list_of_letters.append(test_string)

    iterator: int = 0
    while iterator < len(list_of_letters):
        current_letter = list_of_letters[iterator]
        count_current = 0
        inner_index = 0
        while inner_index < len(list_of_letters):
            if list_of_letters[inner_index] == current_letter:
                count_current += 1
            inner_index += 1
        if count_current > maximum_count and current_letter != "":
            maximum_count = count_current
        iterator += 1

    if maximum_count > 0:
        outer_index = 0
        while outer_index < len(list_of_letters):
            candidate_letter = list_of_letters[outer_index]
            candidate_count = 0
            for inner_index2 in range(len(list_of_letters)):
                if list_of_letters[inner_index2] == candidate_letter:
                    candidate_count += 1
            if candidate_count == maximum_count:
                frequency_dictionary[candidate_letter] = maximum_count
            outer_index += 1

    return frequency_dictionary