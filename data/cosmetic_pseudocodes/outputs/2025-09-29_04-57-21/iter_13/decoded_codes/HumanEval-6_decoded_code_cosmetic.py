from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth_counter: int = 0
        depth_peak: int = 0

        def iterate_chars(char_list: List[str], index: int) -> int:
            if index == len(char_list):
                return depth_peak

            nonlocal depth_counter, depth_peak
            if char_list[index] == '(':
                depth_counter += 1
                if depth_counter > depth_peak:
                    depth_peak = depth_counter
            else:
                depth_counter -= 1

            return iterate_chars(char_list, index + 1)

        characters_list = list(group_string)
        return iterate_chars(characters_list, 0)

    segments = parentheses_string.split(' ')
    filtered_segments = [seg for seg in segments if seg != '']

    def map_parse(segment_list: List[str], idx: int) -> List[int]:
        if idx == len(segment_list):
            return []
        return [parse_paren_group(segment_list[idx])] + map_parse(segment_list, idx + 1)

    return map_parse(filtered_segments, 0)