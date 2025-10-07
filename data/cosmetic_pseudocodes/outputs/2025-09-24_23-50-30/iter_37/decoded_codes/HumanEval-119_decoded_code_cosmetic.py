from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def recursive_check(chars: str, depth: int) -> bool:
            if not chars:
                return depth == 0
            head_char, rest_chars = chars[0], chars[1:]
            new_depth = depth + 1 if head_char == '(' else depth - 1
            if new_depth < 0:
                return False
            return recursive_check(rest_chars, new_depth)
        return recursive_check(string_to_verify, 0)

    combined_alpha = list_of_two_strings[0] + list_of_two_strings[1]
    combined_beta = list_of_two_strings[1] + list_of_two_strings[0]
    return 'Yes' if check(combined_alpha) or check(combined_beta) else 'No'