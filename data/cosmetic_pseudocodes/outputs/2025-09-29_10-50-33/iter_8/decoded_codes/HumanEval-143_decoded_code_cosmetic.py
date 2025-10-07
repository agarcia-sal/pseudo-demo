from typing import List


def words_in_sentence(sentence: str) -> str:
    def collect_filtered(accumulator: List[str], tokens: List[str], index: int) -> str:
        if index >= len(tokens):
            return " ".join(accumulator)
        candidate_word = tokens[index]
        marker = False
        if len(candidate_word) == 1:
            marker = True

        def divisor_checker(divisor: int) -> bool:
            if divisor >= len(candidate_word):
                return False
            if len(candidate_word) % divisor == 0:
                return True
            return divisor_checker(divisor + 1)

        if divisor_checker(2):
            marker = True
        if not marker or len(candidate_word) == 2:
            return collect_filtered(accumulator + [candidate_word], tokens, index + 1)
        else:
            return collect_filtered(accumulator, tokens, index + 1)

    splitted_words = sentence.split(" ")
    return collect_filtered([], splitted_words, 0)