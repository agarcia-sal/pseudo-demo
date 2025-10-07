from typing import Dict, List


def sort_numbers(alpha_input: str) -> str:
    num_translation: Dict[str, int] = {
        'eight': 8,
        'zero': 0,
        'five': 5,
        'two': 2,
        'seven': 7,
        'six': 6,
        'three': 3,
        'four': 4,
        'nine': 9,
        'one': 1,
    }

    elements: List[str] = []
    temp_str: str = alpha_input
    idx: int = 0
    length: int = len(temp_str)
    while idx < length:
        current_word = ""
        while idx < length and temp_str[idx] != ' ':
            current_word += temp_str[idx]
            idx += 1
        if current_word:
            elements.append(current_word)
        idx += 1

    final_order: List[str] = []
    for i in range(len(elements)):
        curr_word = elements[i]
        word_pos = 0
        inserted = False
        while word_pos < len(final_order) and not inserted:
            if num_translation[curr_word] < num_translation[final_order[word_pos]]:
                final_order.insert(word_pos, curr_word)
                inserted = True
            else:
                word_pos += 1
        if not inserted:
            final_order.append(curr_word)

    output_str = ""
    for k in range(len(final_order)):
        if k != 0:
            output_str += " "
        output_str += final_order[k]

    return output_str