from typing import List


def anti_shuffle(original_text: str) -> str:
    temp_collection: List[str] = []
    word_collection: List[str] = original_text.split(" ")
    idx: int = 0
    while idx < len(word_collection):
        current_element: str = word_collection[idx]
        char_array: List[str] = []
        cix: int = 0
        while cix < len(current_element):
            char_array.append(current_element[cix])
            cix += 1
        i: int = 0
        while i < len(char_array) - 1:
            j: int = 0
            while j < len(char_array) - 1 - i:
                if char_array[j] > char_array[j + 1]:
                    temp_var = char_array[j]
                    char_array[j] = char_array[j + 1]
                    char_array[j + 1] = temp_var
                j += 1
            i += 1
        rebuilt_word: str = ""
        k: int = 0
        while k < len(char_array):
            rebuilt_word += char_array[k]
            k += 1
        temp_collection.append(rebuilt_word)
        idx += 1
    output_text: str = ""
    m: int = 0
    length_temp: int = len(temp_collection)
    while m < length_temp:
        output_text += temp_collection[m]
        if m < length_temp - 1:
            output_text += " "
        m += 1
    return output_text