from typing import List

def words_string(sequence_input: str) -> List[str]:
    def process_index(pos: int, acc_chars: List[str]) -> List[str]:
        if pos >= len(sequence_input):
            return acc_chars
        current_char = sequence_input[pos]
        new_acc = acc_chars + ([' '] if current_char == ',' else [current_char])
        return process_index(pos + 1, new_acc)

    if len(sequence_input) == 0:
        return []
    final_chars = process_index(0, [])
    combined_str = "".join(final_chars)
    return combined_str.split()