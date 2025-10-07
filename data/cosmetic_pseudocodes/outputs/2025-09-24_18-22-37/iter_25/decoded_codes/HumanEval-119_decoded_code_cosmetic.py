from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter_var: int = 0
        index_var: int = 0
        length: int = len(string_to_verify)

        while index_var < length:
            current_char: str = string_to_verify[index_var]
            if current_char == '(':
                counter_var += 1
            else:
                counter_var -= 1

            if counter_var < 0:
                return False

            index_var += 1

        return counter_var == 0

    part_a: str = list_of_two_strings[0]
    part_b: str = list_of_two_strings[1]

    first_concat: str = part_a + part_b
    second_concat: str = part_b + part_a

    result_one: bool = check(first_concat)
    result_two: bool = check(second_concat)

    if result_one or result_two:
        return 'Yes'
    else:
        return 'No'