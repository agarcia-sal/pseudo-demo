from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    counter: int = 0
    while counter < integer_n:
        remainder_11 = counter - ((counter // 11) * 11)
        remainder_13 = counter - ((counter // 13) * 13)
        if remainder_11 == 0:
            collected_values.append(counter)
        else:
            if remainder_13 == 0:
                collected_values.append(counter)
        counter += 1

    output_text: str = ""
    index_var: int = 0
    while index_var < len(collected_values):
        num_str = str(collected_values[index_var])
        output_text += num_str
        index_var += 1

    tally_seven: int = 0
    pointer_char: int = 0
    while pointer_char < len(output_text):
        if output_text[pointer_char] == '7':
            tally_seven += 1
        pointer_char += 1

    return tally_seven