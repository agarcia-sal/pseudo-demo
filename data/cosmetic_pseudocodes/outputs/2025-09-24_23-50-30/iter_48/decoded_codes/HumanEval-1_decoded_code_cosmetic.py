from typing import List

def separate_paren_groups(renamed_param: str) -> List[str]:
    accumulator: List[str] = []
    buffer_collector: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0
    length_counter: int = len(renamed_param)

    while index_counter != length_counter:
        current_symbol: str = renamed_param[index_counter]

        if current_symbol != ')' and current_symbol == '(':
            depth_counter += 1
            buffer_collector.append(current_symbol)
        elif current_symbol == ')':
            depth_counter -= 1
            buffer_collector.append(current_symbol)
            if depth_counter == 0:
                accumulator.append("".join(buffer_collector))
                buffer_collector.clear()
        else:
            pass  # no action on other characters

        index_counter += 1

    return accumulator