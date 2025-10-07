from typing import List


def anti_shuffle(memo_text: str) -> str:
    tokens_sequence: List[str] = []
    idx_counter: int = 1

    # Tokenize memo_text by spaces
    while idx_counter <= len(memo_text):
        char_limiter = memo_text[idx_counter - 1]  # 1-based index in pseudocode
        if char_limiter == ' ':
            tokens_sequence.append(memo_text[: idx_counter - 1])
            memo_text = memo_text[idx_counter :]
            idx_counter = 0
        idx_counter += 1
    if len(memo_text) > 0:
        tokens_sequence.append(memo_text)

    processed_collection: List[str] = []
    position_marker: int = 0

    while position_marker < len(tokens_sequence):
        current_string = tokens_sequence[position_marker]
        character_array: List[str] = []
        pointer_kappa: int = 1

        # Build character array from current_string
        while pointer_kappa <= len(current_string):
            character_array.append(current_string[pointer_kappa - 1])
            pointer_kappa += 1

        sorted_character_array: List[str] = []

        # Selection sort characters in character_array into sorted_character_array
        while len(character_array) > 0:
            smallest_elem = character_array[0]
            index_to_remove = 0
            checker_iota = 1
            while checker_iota < len(character_array):
                if character_array[checker_iota] < smallest_elem:
                    smallest_elem = character_array[checker_iota]
                    index_to_remove = checker_iota
                checker_iota += 1
            sorted_character_array.append(smallest_elem)
            character_array.pop(index_to_remove)

        rebuilt_token: str = ''
        iter_lamda: int = 1
        while iter_lamda <= len(sorted_character_array):
            rebuilt_token += sorted_character_array[iter_lamda - 1]
            iter_lamda += 1

        processed_collection.append(rebuilt_token)
        position_marker += 1

    aggregated_result: str = ''
    index_omega: int = 1
    while index_omega <= len(processed_collection):
        aggregated_result += processed_collection[index_omega - 1]
        if index_omega < len(processed_collection):
            aggregated_result += ' '
        index_omega += 1

    return aggregated_result