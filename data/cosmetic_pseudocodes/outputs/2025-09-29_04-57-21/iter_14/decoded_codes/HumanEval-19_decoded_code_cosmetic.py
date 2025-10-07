from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    numeral_values: Dict[str, int] = {
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

    extracted_terms: list[str] = []
    pos: int = 0
    length: int = len(string_of_number_words)
    while pos < length:
        start_idx = pos
        while pos < length and string_of_number_words[pos] != ' ':
            pos += 1
        if start_idx != pos:
            extracted_terms.append(string_of_number_words[start_idx:pos])
        pos += 1

    def compare_words(a: str, b: str) -> int:
        return numeral_values[a] - numeral_values[b]

    sorted_terms = extracted_terms[:]
    n = len(sorted_terms)
    for i in range(n):
        for j in range(n - i - 1):
            if compare_words(sorted_terms[j], sorted_terms[j + 1]) > 0:
                sorted_terms[j], sorted_terms[j + 1] = sorted_terms[j + 1], sorted_terms[j]

    output_string = ''
    indexer = 0
    while indexer < n:
        output_string += sorted_terms[indexer]
        if indexer < n - 1:
            output_string += ' '
        indexer += 1

    return output_string