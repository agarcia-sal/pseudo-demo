from typing import List, Tuple

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def recurse(index_state: Tuple[int, int]) -> bool:
            pos, bal = index_state
            if pos >= len(string_to_verify):
                return bal == 0
            current_char = string_to_verify[pos]
            new_bal = bal + (1 if current_char == '(' else -1)
            if new_bal < 0:
                return False
            return recurse((pos + 1, new_bal))
        return recurse((0, 0))

    concat_alpha = list_of_two_strings[0] + list_of_two_strings[1]
    concat_beta = list_of_two_strings[1] + list_of_two_strings[0]
    return 'Yes' if check(concat_alpha) else ('Yes' if check(concat_beta) else 'No')