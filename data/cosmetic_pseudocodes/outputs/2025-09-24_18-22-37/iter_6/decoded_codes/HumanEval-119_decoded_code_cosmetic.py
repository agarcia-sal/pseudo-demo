from typing import List

def match_parens(collection_of_strings: List[str]) -> str:
    def check(sequence_to_test: str) -> bool:
        count_balance = 0
        for current_symbol in sequence_to_test:
            if current_symbol == '(':
                count_balance += 1
            else:
                count_balance -= 1
            if count_balance < 0:
                return False
        return count_balance == 0

    combo_first = collection_of_strings[0] + collection_of_strings[1]
    combo_second = collection_of_strings[1] + collection_of_strings[0]
    if check(combo_first):
        return 'Yes'
    if check(combo_second):
        return 'Yes'
    return 'No'