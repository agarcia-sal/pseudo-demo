from typing import List


def anti_shuffle(input_string: str) -> str:
    temp_sequence: List[str] = []
    idx: int = 0
    words_array: List[str] = input_string.split(" ")
    while idx < len(words_array):
        current: str = words_array[idx]
        char_array: List[str] = []
        position: int = 0
        while position < len(current):
            char_array.append(current[position])
            position += 1
        char_array.sort()
        reconstructed: str = ""
        pointer: int = 0
        while pointer < len(char_array):
            reconstructed += char_array[pointer]
            pointer += 1
        temp_sequence.append(reconstructed)
        idx += 1
    output_line: str = ""
    q: int = 0
    while q < len(temp_sequence):
        output_line += temp_sequence[q]
        if q != len(temp_sequence) - 1:
            output_line += " "
        q += 1
    return output_line