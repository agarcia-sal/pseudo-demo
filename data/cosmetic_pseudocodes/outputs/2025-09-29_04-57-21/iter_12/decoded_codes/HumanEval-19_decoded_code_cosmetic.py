from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    number_dictionary: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    temp_word_list: List[str] = string_of_number_words.split(' ')
    filtered_words: List[str] = [word for word in temp_word_list if len(word) != 0]

    def compare_words(a: str, b: str) -> bool:
        return number_dictionary[a] <= number_dictionary[b]

    def insertion_sort(lst: List[str]) -> List[str]:
        i = 1
        while i < len(lst):
            key = lst[i]
            j = i - 1
            while j >= 0 and number_dictionary[lst[j]] > number_dictionary[key]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
            i += 1
        return lst

    sorted_words: List[str] = insertion_sort(filtered_words)
    return ' '.join(sorted_words)