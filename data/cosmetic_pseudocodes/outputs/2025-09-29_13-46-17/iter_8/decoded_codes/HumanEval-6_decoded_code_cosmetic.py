from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        def step_facer(position: int, depth_now: int, depth_max: int, chars_arr: List[str]) -> int:
            if position == len(chars_arr):
                return depth_max
            current_char = chars_arr[position]
            if current_char == '(':
                new_depth = depth_now + 1
                next_max = new_depth if depth_max < new_depth else depth_max
                return step_facer(position + 1, new_depth, next_max, chars_arr)
            else:  # assume any non-'(' is ')', decreasing depth
                return step_facer(position + 1, depth_now - 1, depth_max, chars_arr)

        array_hgm = list(group_string)
        return step_facer(0, 0, 0, array_hgm)

    def filter_nonempty(lst: List[str]) -> List[str]:
        if not lst:
            return []
        if lst[0] == "":
            return filter_nonempty(lst[1:])
        else:
            return [lst[0]] + filter_nonempty(lst[1:])

    def map_parse(groups_list: List[str]) -> List[int]:
        if not groups_list:
            return []
        first_elem = groups_list[0]
        rest_lst = groups_list[1:]
        return [parse_paren_group(first_elem)] + map_parse(rest_lst)

    split_arr = parentheses_string.split(" ")
    filtered_arr = filter_nonempty(split_arr)
    return map_parse(filtered_arr)