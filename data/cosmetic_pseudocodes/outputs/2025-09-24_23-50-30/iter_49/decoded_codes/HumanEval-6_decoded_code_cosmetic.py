from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def recur_parse(index_cursor: int, current_counter: int, highest_counter: int) -> int:
            if index_cursor == len(group_string):
                return highest_counter
            char_x = group_string[index_cursor]
            next_counter = current_counter + 1 if char_x == '(' else current_counter - 1
            next_highest = next_counter if next_counter > highest_counter else highest_counter
            return recur_parse(index_cursor + 1, next_counter, next_highest)

        return recur_parse(0, 0, 0)

    def filter_map_nonempty(input_array: List[str]) -> List[int]:
        def helper_loop(pos: int, acc: List[int]) -> List[int]:
            if pos == len(input_array):
                return acc
            elem_x = input_array[pos]
            if elem_x == '':
                return helper_loop(pos + 1, acc)
            return helper_loop(pos + 1, acc + [parse_paren_group(elem_x)])

        return helper_loop(0, [])

    segments_arr = parentheses_string.split(' ')
    return filter_map_nonempty(segments_arr)