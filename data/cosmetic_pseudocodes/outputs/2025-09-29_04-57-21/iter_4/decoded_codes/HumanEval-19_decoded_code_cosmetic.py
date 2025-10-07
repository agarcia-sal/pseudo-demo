from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    digitValues: dict[str, int] = {
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
    wordsCollection: List[str] = [token for token in string_of_number_words.split(' ') if token != '']

    def comparator(a: str, b: str) -> bool:
        return digitValues[a] > digitValues[b]

    i: int = 0
    n: int = len(wordsCollection)
    while i < n - 1:
        j: int = 0
        while j < n - i - 1:
            if comparator(wordsCollection[j], wordsCollection[j + 1]):
                wordsCollection[j], wordsCollection[j + 1] = wordsCollection[j + 1], wordsCollection[j]
            j += 1
        i += 1

    outputString: str = ''
    index: int = 0
    while index < len(wordsCollection):
        outputString += wordsCollection[index]
        if index < len(wordsCollection) - 1:
            outputString += ' '
        index += 1

    return outputString