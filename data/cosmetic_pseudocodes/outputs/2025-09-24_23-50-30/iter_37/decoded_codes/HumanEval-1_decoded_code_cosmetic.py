from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collection_of_fragments: List[str] = []
    temp_buffer: List[str] = []
    depth_counter: int = 0

    def process(index: int) -> None:
        if index == len(string_of_parentheses):
            return

        symbol = string_of_parentheses[index]

        if symbol == '(':
            nonlocal depth_counter
            depth_counter += 1
            temp_buffer.append(symbol)
        elif symbol == ')':
            nonlocal depth_counter
            depth_counter -= 1
            temp_buffer.append(symbol)
            if depth_counter == 0:
                collection_of_fragments.append(''.join(temp_buffer))
                temp_buffer.clear()
        # default case: no operation

        process(index + 1)

    process(0)
    return collection_of_fragments