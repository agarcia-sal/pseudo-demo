from typing import List


def parse_nested_parens(spaced_parentheses: str) -> List[int]:
    def parse_paren_group(inner_sequence: str) -> int:
        def recursive_count(chars: str, index: int, depth_acc: int, max_acc: int) -> int:
            if index == len(chars):
                return max_acc
            current_char = chars[index]
            updated_depth = depth_acc + (1 if current_char == '(' else -1)
            updated_max = updated_depth if updated_depth > max_acc else max_acc
            return recursive_count(chars, index + 1, updated_depth, updated_max)

        return recursive_count(inner_sequence, 0, 0, 0)

    split_groups = [x for x in spaced_parentheses.split(' ') if len(x) > 0]
    result_list: List[int] = []
    for element in split_groups:
        result_list.append(parse_paren_group(element))
    return result_list