from typing import List

def match_parens(arr_two_strs: List[str]) -> str:
    def validate(seq_input: str) -> bool:
        def recur(index_loc: int, bal_accum: int) -> bool:
            if index_loc >= len(seq_input):
                return bal_accum == 0
            sym = seq_input[index_loc]
            next_bal = bal_accum + (1 if sym == '(' else -1)
            if next_bal < 0:
                return False
            return recur(index_loc + 1, next_bal)
        return recur(0, 0)

    pair_one = arr_two_strs[0] + arr_two_strs[1]
    pair_two = arr_two_strs[1] + arr_two_strs[0]

    return 'Yes' if validate(pair_one) or validate(pair_two) else 'No'