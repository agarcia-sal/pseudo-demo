from typing import List

def words_string(text_param: str) -> List[str]:
    def process_chars(index_param: int, acc_list: List[str]) -> List[str]:
        if index_param >= len(text_param):
            return acc_list
        curr_char = text_param[index_param]
        updated_list = acc_list + ([' '] if curr_char == ',' else [curr_char])
        return process_chars(index_param + 1, updated_list)

    if text_param == "":
        return []
    transformed_list = process_chars(0, [])
    merged_str = "".join(transformed_list)

    filtered_words: List[str] = []
    start_idx = 0
    length_str = len(merged_str)

    while start_idx < length_str:
        while start_idx < length_str and merged_str[start_idx] == ' ':
            start_idx += 1
        if start_idx >= length_str:
            break
        end_idx = start_idx
        while end_idx < length_str and merged_str[end_idx] != ' ':
            end_idx += 1
        filtered_words.append(merged_str[start_idx:end_idx])
        start_idx = end_idx

    return filtered_words