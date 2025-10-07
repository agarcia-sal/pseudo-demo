from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    gathered_numbers: List[int] = []
    words: List[str] = string_description.split(" ")
    index: int = 0
    while index < len(words):
        current_word = words[index]
        if current_word.isdigit():
            gathered_numbers.append(int(current_word))
        # default case does nothing
        index += 1
    sum_of_numbers = 0
    pointer = 0
    while pointer < len(gathered_numbers):
        sum_of_numbers += gathered_numbers[pointer]
        pointer += 1
    return total_number_of_fruits - sum_of_numbers