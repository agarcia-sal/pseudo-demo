from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    # Helper function to verify balanced parentheses without negative balance at any point
    def check(string_to_verify: str) -> bool:
        deficit = False
        balance = 0
        index = 0
        while index < len(string_to_verify) and not deficit:
            current_char = string_to_verify[index]
            balance += 1 if current_char == '(' else -1
            if balance < 0:
                deficit = True
            index += 1
        return balance == 0 and not deficit

    pair_one = list_of_two_strings[1] + list_of_two_strings[0]
    pair_two = list_of_two_strings[0] + list_of_two_strings[1]
    if check(pair_two) or check(pair_one):
        return "Yes"
    return "No"