from typing import List


def words_string(param_str: str) -> List[str]:
    def proc_transform_chars(src_str: str, idx: int, acc_list: List[str]) -> List[str]:
        if idx >= len(src_str):
            return acc_list
        current_char = src_str[idx]
        if current_char == ',':
            new_acc = acc_list + [' ']
        else:
            new_acc = acc_list + [current_char]
        return proc_transform_chars(src_str, idx + 1, new_acc)

    if not (len(param_str) > 0):
        return []

    accumulator = proc_transform_chars(param_str, 0, [])

    def func_join_characters(char_arr: List[str]) -> str:
        res = ""
        for n in range(len(char_arr)):
            res += char_arr[n]
        return res

    composed_string = func_join_characters(accumulator)

    def func_split_by_whitespace(s: str) -> List[str]:
        words_temp: List[str] = []
        pos_start = 0
        pos_end = 0
        length = len(s)
        while pos_end < length:
            if s[pos_end] in {' ', '\t', '\n'}:
                if pos_start < pos_end:
                    words_temp.append(s[pos_start:pos_end])
                pos_start = pos_end + 1
            pos_end += 1
        if pos_start < pos_end:
            words_temp.append(s[pos_start:pos_end])
        return words_temp

    return func_split_by_whitespace(composed_string)