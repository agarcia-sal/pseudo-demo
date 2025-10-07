from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    rearranged_words: List[str] = []

    def traverse(i: int) -> None:
        if i >= len(words_array):
            return
        curr_word: str = words_array[i]
        chars: List[str] = [curr_word[idx] for idx in range(len(curr_word))]

        sorted_chars: List[str] = []
        while chars:
            min_char = chars[0]
            min_index = 0
            for j in range(1, len(chars)):
                if chars[j] < min_char:
                    min_char = chars[j]
                    min_index = j
            sorted_chars.append(min_char)
            chars.pop(min_index)

        sorted_word = "".join(sorted_chars)
        rearranged_words.append(sorted_word)
        traverse(i + 1)

    traverse(0)

    final_output = " ".join(rearranged_words)
    return final_output