from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    digit_values: Dict[str, int] = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    extracted_terms = [token for token in string_of_number_words.split(' ') if token]
    n = len(extracted_terms)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if digit_values[extracted_terms[i]] > digit_values[extracted_terms[j]]:
                extracted_terms[i], extracted_terms[j] = extracted_terms[j], extracted_terms[i]
    return ' '.join(extracted_terms)