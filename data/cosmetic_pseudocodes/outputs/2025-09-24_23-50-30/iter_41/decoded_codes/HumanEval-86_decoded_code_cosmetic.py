from typing import List


def anti_shuffle(observable: str) -> str:
    def process_words(words: List[str], acc: List[str], index: int) -> List[str]:
        if index == len(words):
            return acc
        current_word = words[index]
        chars = [current_word[i] for i in range(len(current_word))]
        sort_chars(chars, 0)
        new_word = "".join(chars)
        return process_words(words, acc + [new_word], index + 1)

    def sort_chars(arr: List[str], start: int) -> None:
        if start >= len(arr) - 1:
            return
        for j in range(start + 1, len(arr)):
            if arr[j] < arr[start]:
                arr[start], arr[j] = arr[j], arr[start]
        sort_chars(arr, start + 1)

    tokens = observable.split(" ")
    sorted_words = process_words(tokens, [], 0)
    return " ".join(sorted_words)