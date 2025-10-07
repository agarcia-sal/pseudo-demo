from typing import List


def anti_shuffle(alphanumeric_sequence: str) -> str:
    CharArray = List[str]

    word_collection: List[str]
    index_tracker: int = 0
    collected_sorted_words: List[str] = []
    assembled_result: str

    def sort_characters_recursively(arr: CharArray, left_bound: int, right_bound: int) -> CharArray:
        if left_bound >= right_bound:
            return arr
        pivot: str = arr[right_bound]
        marker: int = left_bound - 1

        def partition_loop(position: int, pivot_char: str, boundary: int, marker_val: int) -> int:
            if position > boundary - 1:
                return marker_val
            if not (arr[position] > pivot_char):
                marker_val += 1
                arr[marker_val], arr[position] = arr[position], arr[marker_val]
            return partition_loop(position + 1, pivot_char, boundary, marker_val)

        marker = partition_loop(left_bound, pivot, right_bound, marker)
        arr[marker + 1], arr[right_bound] = arr[right_bound], arr[marker + 1]

        arr = sort_characters_recursively(arr, left_bound, marker)
        arr = sort_characters_recursively(arr, marker + 2, right_bound)
        return arr

    def process_words(position: int, words_list: List[str], results: List[str]) -> List[str]:
        if position >= len(words_list):
            return results
        current_word: str = words_list[position]
        chars_of_word: CharArray = []

        def string_to_char_array(s: str, pos: int, arr: CharArray) -> CharArray:
            if pos >= len(s):
                return arr
            arr.append(s[pos])
            return string_to_char_array(s, pos + 1, arr)

        chars_of_word = string_to_char_array(current_word, 0, [])
        chars_of_word = sort_characters_recursively(chars_of_word, 0, len(chars_of_word) - 1)

        def char_array_to_string(arr: CharArray, pos: int, accum: str) -> str:
            if pos >= len(arr):
                return accum
            return char_array_to_string(arr, pos + 1, accum + arr[pos])

        sorted_word: str = char_array_to_string(chars_of_word, 0, "")
        results.append(sorted_word)
        return process_words(position + 1, words_list, results)

    def split_string_to_list(s: str, current_pos: int, res_list: List[str], word_accum: str) -> List[str]:
        if current_pos >= len(s):
            if len(word_accum) > 0:
                res_list.append(word_accum)
            return res_list
        current_char: str = s[current_pos]
        if current_char == ' ':
            if len(word_accum) > 0:
                res_list.append(word_accum)
                word_accum = ""
        else:
            word_accum += current_char
        return split_string_to_list(s, current_pos + 1, res_list, word_accum)

    word_collection = split_string_to_list(alphanumeric_sequence, 0, [], "")
    collected_sorted_words = process_words(0, word_collection, [])

    def join_list_with_space(lst: List[str], pos: int, acc_string: str) -> str:
        if pos >= len(lst):
            return acc_string
        if pos == 0:
            updated_string = lst[pos]
        else:
            updated_string = acc_string + " " + lst[pos]
        return join_list_with_space(lst, pos + 1, updated_string)

    assembled_result = join_list_with_space(collected_sorted_words, 0, "")
    return assembled_result