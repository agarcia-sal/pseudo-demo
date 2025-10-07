from typing import List


def anti_shuffle(input_string: str) -> str:
    idx: int = 0
    words: List[str] = input_string.split(" ")
    transformed: List[str] = []

    def recursive_process() -> None:
        nonlocal idx
        if idx >= len(words):
            return

        token = words[idx]
        letters = list(token)

        i = 1
        while i < len(letters):
            j = i
            while j > 0 and letters[j - 1] > letters[j]:
                letters[j - 1], letters[j] = letters[j], letters[j - 1]  # swap
                j -= 1
            i += 1

        sorted_token = "".join(letters)
        transformed.append(sorted_token)
        idx += 1
        recursive_process()

    recursive_process()

    output_string = " ".join(transformed)
    return output_string