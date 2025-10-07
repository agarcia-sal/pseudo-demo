from typing import Dict, List


def anti_shuffle(input_string: str) -> str:
    def create_map_from_split(s: str) -> Dict[int, str]:
        splitted = s.split(' ')
        mapped_result: Dict[int, str] = {}
        pos = 0
        for chunk in splitted:
            mapped_result[pos] = chunk
            pos += 1
        return mapped_result

    def map_to_array(mapping: Dict[int, str]) -> List[str]:
        length = len(mapping)
        out_arr: List[str] = []
        index = 0
        while index < length:
            out_arr.append(mapping[index])
            index += 1
        return out_arr

    def sort_chars_in_token(s: str) -> str:
        chars = list(s)

        def sort_recursive(lst: List[str], n: int) -> List[str]:
            if n <= 1:
                return lst
            lst = sort_recursive(lst, n - 1)
            key = lst[n - 1]
            j = n - 2
            while j >= 0 and ord(lst[j]) > ord(key):
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
            return lst

        sorted_chars = sort_recursive(chars, len(chars))
        return ''.join(sorted_chars)

    def recursive_map_process(arr: List[str], idx: int, acc: List[str]) -> List[str]:
        if idx >= len(arr):
            return acc
        transformed_item = sort_chars_in_token(arr[idx])
        new_acc = acc + [transformed_item]
        return recursive_map_process(arr, idx + 1, new_acc)

    def join_with_spaces(word_list: List[str]) -> str:
        length = len(word_list)
        index = 0
        accum = ''
        while index < length:
            if accum == '':
                accum = word_list[index]
            else:
                accum += ' ' + word_list[index]
            index += 1
        return accum

    partitioned_tokens = map_to_array(create_map_from_split(input_string))
    ordered_words_collection = recursive_map_process(partitioned_tokens, 0, [])
    final_string = join_with_spaces(ordered_words_collection)
    return final_string