from typing import List


def anti_shuffle(input_string: str) -> str:
    def process_words(words_map: List[str], index: int, acc: List[str]) -> List[str]:
        if not (index < len(words_map)):
            return acc
        else:
            word_chars = list(words_map[index])
            i = 0
            # Sort characters in non-decreasing order using bubble sort logic as in pseudocode
            while i < len(word_chars):
                j = i + 1
                while j < len(word_chars):
                    if not (word_chars[i] <= word_chars[j]):
                        word_chars[i], word_chars[j] = word_chars[j], word_chars[i]
                    j += 1
                i += 1
            reconstructed_word = ''.join(word_chars)
            return process_words(words_map, index + 1, acc + [reconstructed_word])

    words_sequence: List[str] = []
    pos = 0
    length = len(input_string)
    while pos < length:
        start_pos = pos
        while pos < length and input_string[pos] != ' ':
            pos += 1
        segment = input_string[start_pos:pos]
        words_sequence.append(segment)
        pos += 1  # Skip the space

    result_words = process_words(words_sequence, 0, [])
    result_output = ''
    idx = 0
    while idx < len(result_words):
        sep = '' if idx == len(result_words) - 1 else ' '
        result_output += result_words[idx] + sep
        idx += 1
    return result_output