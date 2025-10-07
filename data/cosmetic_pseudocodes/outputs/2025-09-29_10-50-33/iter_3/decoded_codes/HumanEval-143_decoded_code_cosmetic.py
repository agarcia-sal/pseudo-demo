from typing import List


def words_in_sentence(sentence: str) -> str:
    filtered_words: List[str] = []
    split_words: List[str] = sentence.split(" ")
    idx_outer: int = 0

    while idx_outer < len(split_words):
        token: str = split_words[idx_outer]
        marker: int = 0

        if len(token) != 1:
            divisor: int = 2

            while divisor < (len(token) - 1):
                if (len(token) % divisor) == 0:
                    marker = 1
                divisor += 1
        else:
            marker = 1

        if (marker == 0) or (len(token) == 2):
            filtered_words.append(token)

        idx_outer += 1

    return " ".join(filtered_words)