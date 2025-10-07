from typing import List

def anti_shuffle(input_string: str) -> str:
    words_list: List[str] = input_string.split(" ")
    transformed_words: List[str] = [
        "".join(sorted(list(item))) for item in words_list
    ]
    return " ".join(transformed_words)