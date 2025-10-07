from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def process_chars(
        chars: List[str],
        index: int,
        depth_accum: int,
        collected: List[str],
        final_groups: List[str]
    ) -> List[str]:
        if index == len(chars):
            return final_groups

        current_char = chars[index]

        if current_char == '(':
            depth_accum += 1
            collected.append(current_char)
        elif current_char == ')':
            depth_accum -= 1
            collected.append(current_char)
            if depth_accum == 0:
                final_groups.append(''.join(collected))
                collected.clear()
        # Characters other than '(' and ')' are ignored

        return process_chars(chars, index + 1, depth_accum, collected, final_groups)

    chars_list = list(string_of_parentheses)
    return process_chars(chars_list, 0, 0, [], [])