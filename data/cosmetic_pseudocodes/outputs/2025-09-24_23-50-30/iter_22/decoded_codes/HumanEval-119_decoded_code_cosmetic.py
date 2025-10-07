from typing import List

def match_parens(pairs_of_strings: List[str]) -> str:
    def check(text_to_eval: str) -> bool:
        tally = 0
        for current in text_to_eval:
            tally = tally + 1 if current == '(' else tally - 1
            if tally < 0:
                return False
        return tally == 0

    first_concat = pairs_of_strings[0] + pairs_of_strings[1]
    second_concat = pairs_of_strings[1] + pairs_of_strings[0]

    if check(first_concat):
        return 'Yes'
    if check(second_concat):
        return 'Yes'
    return 'No'