from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    def replace_commas(s: str, idx: int, acc: str) -> str:
        if idx >= len(s):
            return acc
        ch = s[idx]
        next_acc = acc + (" " if ch == "," else ch)
        return replace_commas(s, idx + 1, next_acc)

    transformed = replace_commas(input_string, 0, "")
    split_words: List[str] = []
    word_start = 0
    i = 0
    length = len(transformed)
    while i <= length:
        if i == length or transformed[i] == " ":
            if word_start < i:
                split_words.append(transformed[word_start:i])
            word_start = i + 1
        i += 1

    return split_words