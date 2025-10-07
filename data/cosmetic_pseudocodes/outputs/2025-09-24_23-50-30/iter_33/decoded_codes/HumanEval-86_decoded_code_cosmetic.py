from typing import List


def anti_shuffle(input_sequence: str) -> str:
    tokens_collection: List[str] = []
    index_counter: int = 0
    length: int = len(input_sequence)

    while index_counter < length:
        start_position = index_counter
        while index_counter < length and input_sequence[index_counter] != ' ':
            index_counter += 1
        if start_position < index_counter:
            tokens_collection.append(input_sequence[start_position:index_counter])
        index_counter += 1

    def reorder_chars(text: str) -> str:
        if len(text) <= 1:
            return text
        pivot_char = text[0]
        lesser_chars = reorder_chars(''.join(c for c in text if c < pivot_char))
        equal_chars = ''.join(c for c in text if c == pivot_char)
        greater_chars = reorder_chars(''.join(c for c in text if c > pivot_char))
        return lesser_chars + equal_chars + greater_chars

    def transform_list(collection: List[str], acc: List[str], pos: int) -> List[str]:
        if pos == len(collection):
            return acc
        current_element = collection[pos]
        sorted_element = reorder_chars(current_element)
        return transform_list(collection, acc + [sorted_element], pos + 1)

    processed_tokens = transform_list(tokens_collection, [], 0)

    def join_with_space(elements: List[str], pos: int, acc_string: str) -> str:
        if pos == len(elements):
            return acc_string
        separator = ' ' if pos > 0 else ''
        return join_with_space(elements, pos + 1, acc_string + separator + elements[pos])

    return join_with_space(processed_tokens, 0, '')