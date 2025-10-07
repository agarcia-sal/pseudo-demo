from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    mapping_values: Dict[str, int] = {
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

    raw_words = string_of_number_words.split(" ")
    filtered_words = [word for word in raw_words if word != ""]

    def compare_words(a: str, b: str) -> int:
        return mapping_values[a] - mapping_values[b]

    result_list = filtered_words[:]
    n = len(result_list)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if compare_words(result_list[i], result_list[j]) > 0:
                result_list[i], result_list[j] = result_list[j], result_list[i]

    final_string = " ".join(result_list)
    return final_string