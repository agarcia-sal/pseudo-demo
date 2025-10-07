from typing import List


def anti_shuffle(alpha_input: str) -> str:
    token_collection: List[str] = alpha_input.split(" ")
    collection_sorted_tokens: List[str] = []

    idx_iter = 0
    while idx_iter < len(token_collection):
        temp_chars: List[str] = list(token_collection[idx_iter])

        temp_sorted_chars: List[str] = []
        inner_idx = 0

        while inner_idx < len(temp_chars):
            smallest_ascii = 127
            smallest_index = -1
            search_pos = 0

            # Find the character with smallest ASCII value (including ties, choose rightmost)
            while search_pos < len(temp_chars):
                char_ascii = ord(temp_chars[search_pos])
                if char_ascii <= smallest_ascii:
                    smallest_ascii = char_ascii
                    smallest_index = search_pos
                search_pos += 1

            # Remove and add smallest character found
            if smallest_index >= 0:
                temp_sorted_chars.append(temp_chars[smallest_index])
                temp_chars.pop(smallest_index)

            inner_idx += 1

        assembled_token = ""
        build_j = 0
        while build_j < len(temp_sorted_chars):
            assigned_char = temp_sorted_chars[build_j]
            assembled_token += assigned_char
            build_j += 1

        collection_sorted_tokens.append(assembled_token)
        idx_iter += 1

    combined_string = ""
    if len(collection_sorted_tokens) == 0:
        return combined_string

    index_walker = 0

    while True:
        combined_string += collection_sorted_tokens[index_walker]

        if index_walker == len(collection_sorted_tokens) - 1:
            break

        combined_string += " "

        index_walker += 1

    return combined_string