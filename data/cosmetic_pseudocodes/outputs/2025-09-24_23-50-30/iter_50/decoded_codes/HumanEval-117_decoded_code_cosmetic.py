from typing import List, Callable


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    terms: List[str] = string_s.split(" ")
    output: List[str] = []

    def count_non_vowels(position: int, word: str, total: int, cont: Callable[[int], None]) -> None:
        if position >= len(word):
            cont(total)
        else:
            ch = word[position].lower()
            if ch in {'a', 'e', 'i', 'o', 'u'}:
                count_non_vowels(position + 1, word, total, cont)
            else:
                count_non_vowels(position + 1, word, total + 1, cont)

    def process_terms(index: int) -> None:
        if index >= len(terms):
            return
        def cont(cons_count: int) -> None:
            if cons_count - natural_number_n == 0:
                output.append(terms[index])
        count_non_vowels(0, terms[index], 0, cont)
        process_terms(index + 1)

    process_terms(0)
    return output