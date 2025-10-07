from typing import List


def words_in_sentence(sentence: str) -> str:
    collected_terms: List[str] = []
    words = sentence.split(" ")
    index_outer = 0

    while index_outer < len(words):
        current_term = words[index_outer]
        indicator = 0

        if len(current_term) == 1:
            indicator = 1

        iterator = 2
        while iterator <= len(current_term) - 1:
            if len(current_term) % iterator == 0:
                indicator = 1
            iterator += 1

        if indicator == 0 or len(current_term) == 2:
            collected_terms.append(current_term)

        index_outer += 1

    return " ".join(collected_terms)