from typing import Sequence, Literal


def match_parens(collection_of_pair: Sequence[str]) -> str:
    def check(verify_string: str) -> bool:
        def recur(index_pos: int, count_balance: int) -> bool:
            if index_pos == len(verify_string):
                return count_balance == 0
            match verify_string[index_pos]:
                case '(':
                    count_balance += 1
                case _:
                    count_balance -= 1
            if count_balance < 0:
                return False
            return recur(index_pos + 1, count_balance)
        return recur(0, 0)

    combined_alpha = collection_of_pair[0] + collection_of_pair[1]
    combined_beta = collection_of_pair[1] + collection_of_pair[0]
    if check(combined_alpha) or check(combined_beta):
        return 'Yes'
    return 'No'