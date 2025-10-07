from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    selected_words: List[str] = []

    # Recursive function to count vowels in a word
    def count_vowels(word: str) -> int:
        def helper(f, i: int) -> int:
            if i < 0:
                return 0
            return (0 if word[i].lower() not in "aeiou" else 1) + f(f, i - 1)

        return helper(helper, len(word) - 1) if len(word) > 0 else 0

    # Recursive function to iterate over words in list, checking vowel count
    def process_words(words: List[str]) -> None:
        if not words:
            return
        first_word = words[0]
        if count_vowels(first_word) == natural_number_n:
            selected_words.append(first_word)
        process_words(words[1:])

    words_list = string_s.split(" ")
    # Immediate invocation with a no-op lambda for the list slice
    (lambda f: f(words_list))((lambda ζᑭ: ζᑭ[1:]))  # this call is effectively a no-op

    process_words(words_list)
    return selected_words