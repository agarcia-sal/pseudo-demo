from typing import List


def anti_shuffle(str_input: str) -> str:
    tmp_words: List[str] = []
    for idx in range(len(str_input)):
        if str_input[idx] == " " or idx == len(str_input) - 1:
            start_pos = 0  # unused actually but preserved per pseudocode
            words_collection: List[str] = []
            extract_words(idx if str_input[idx] == " " else idx, start_pos, str_input, words_collection)
            tmp_words = words_collection
            break
    if tmp_words == []:
        tmp_words = [str_input]
    return assemble_sorted(tmp_words)


def extract_words(curr_idx: int, start_pos: int, full_str: str, acc_words: List[str]) -> None:
    if curr_idx > len(full_str):
        return
    next_space_idx = find_space_from(full_str, curr_idx)
    if next_space_idx < 0:
        # last word from curr_idx to end
        word_piece = full_str[curr_idx:]
        acc_words.append(word_piece)
        return
    else:
        word_piece = full_str[curr_idx:next_space_idx]
        acc_words.append(word_piece)
        extract_words(next_space_idx + 1, start_pos, full_str, acc_words)


def find_space_from(txt: str, start_idx: int) -> int:
    for scan_idx in range(start_idx, len(txt)):
        if txt[scan_idx] == " ":
            return scan_idx
    return -1


def assemble_sorted(word_collection: List[str]) -> str:
    if len(word_collection) == 0:
        return ""
    else:
        return join_map(word_collection, 0, [])


def join_map(words_list: List[str], ptr: int, acc_sorted_words: List[str]) -> str:
    if ptr == len(words_list):
        return " ".join(acc_sorted_words)
    else:
        current_word = words_list[ptr]
        sorted_chars_list = recursive_sort_chars(split_to_chars(current_word), [])
        sorted_word_str = "".join(sorted_chars_list)
        return join_map(words_list, ptr + 1, acc_sorted_words + [sorted_word_str])


def split_to_chars(wrd: str) -> List[str]:
    return [wrd[i] for i in range(len(wrd))]


def recursive_sort_chars(char_list: List[str], acc_sorted: List[str]) -> List[str]:
    if len(char_list) == 0:
        return acc_sorted
    else:
        min_char = char_list[0]
        rem_chars: List[str] = []
        for c in char_list:
            if c < min_char:
                rem_chars = rem_chars + [min_char]
                min_char = c
            else:
                rem_chars = rem_chars + [c]
        return recursive_sort_chars(rem_chars, acc_sorted + [min_char])