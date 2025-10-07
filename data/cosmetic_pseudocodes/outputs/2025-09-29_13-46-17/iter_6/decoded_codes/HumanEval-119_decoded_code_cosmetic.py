from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def recurse(index_i: int, bal_acc: int) -> bool:
            if index_i < len(string_to_verify):
                char_c = string_to_verify[index_i]
                updated_bal = bal_acc + ((char_c == '(') * 2 - 1)
                if updated_bal < 0:
                    return False
                else:
                    return recurse(index_i + 1, updated_bal)
            else:
                return bal_acc == 0

        return recurse(0, 0)

    first_concat = "{}{}".format(list_of_two_strings[0], list_of_two_strings[1])
    second_concat = "{}{}".format(list_of_two_strings[1], list_of_two_strings[0])

    res_a = check(first_concat)
    res_b = check(second_concat)

    return ("Yes" * (res_a or res_b)) + ("No" * (not (res_a or res_b)))