from typing import List


def anti_shuffle(input_string: str) -> str:
    def process_word_list(words: List[str], index: int, accum: List[str]) -> List[str]:
        if index < len(words):
            current_word = words[index]
            chars_list = list(current_word)
            sorted_chars = merge_sort_asc(chars_list)
            sorted_word = ''.join(sorted_chars)
            return process_word_list(words, index + 1, accum + [sorted_word])
        else:
            return accum

    def merge_sort_asc(arr: List[str]) -> List[str]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_asc(arr[:mid])
        right = merge_sort_asc(arr[mid:])
        return merge(left, right)

    def merge(left: List[str], right: List[str]) -> List[str]:
        result: List[str] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    word_array = input_string.split(" ")
    sorted_words_array = process_word_list(word_array, 0, [])
    # Reduce with string concatenation separated by spaces, handling empty accumulator
    final_string = ""
    for w in sorted_words_array:
        final_string = w if final_string == "" else final_string + " " + w
    return final_string