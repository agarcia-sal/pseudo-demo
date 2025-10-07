from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_dictionary: Dict[str, int] = {}
    list_of_letters = test_string.split(" ")
    max_frequency = 0

    for index in range(len(list_of_letters)):
        current_letter = list_of_letters[index]
        if current_letter != "":
            current_count = 0
            for item in list_of_letters:
                if item == current_letter:
                    current_count += 1
            if current_count > max_frequency:
                max_frequency = current_count

    if max_frequency > 0:
        for i in range(len(list_of_letters)):
            letter = list_of_letters[i]
            if letter != "":
                count_check = 0
                for element in list_of_letters:
                    if element == letter:
                        count_check += 1
                if count_check == max_frequency:
                    frequency_dictionary[letter] = max_frequency

    return frequency_dictionary