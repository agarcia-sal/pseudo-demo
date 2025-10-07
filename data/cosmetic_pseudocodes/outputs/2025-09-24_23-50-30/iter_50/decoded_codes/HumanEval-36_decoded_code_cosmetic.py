from typing import List


def fizz_buzz(integer_n: int) -> int:
    auxiliary_list: List[int] = []

    def build_auxiliary(index_var: int) -> None:
        if not (index_var < integer_n):
            return
        if (index_var % 11 == 0) or (index_var % 13 == 0):
            auxiliary_list.append(index_var)
        build_auxiliary(index_var + 1)

    build_auxiliary(0)

    combined_string: List[str] = []

    def concatenate_all(items: List[int], pos: int) -> None:
        if pos >= len(items):
            return
        combined_string.append(str(items[pos]))
        concatenate_all(items, pos + 1)

    concatenate_all(auxiliary_list, 0)

    def count_char(target_string: str, index_var: int, accumulator: int) -> int:
        if not (index_var < len(target_string)):
            return accumulator
        is_seven_present = target_string[index_var] == '7'
        return count_char(target_string, index_var + 1, accumulator + (1 if is_seven_present else 0))

    return count_char(''.join(combined_string), 0, 0)