from typing import List


def anti_shuffle(input_string: str) -> str:
    def helper(idx: int, tokens: List[str], acc: List[str]) -> List[str]:
        if idx >= len(tokens):
            return acc
        current_token = tokens[idx]
        char_array: List[str] = [c for c in current_token]
        sorted_chars: List[str] = []
        while char_array:
            min_char = char_array[0]
            for ch in char_array:
                if ch < min_char:
                    min_char = ch
            char_array.remove(min_char)
            sorted_chars.append(min_char)
        sorted_token = "".join(sorted_chars)
        if not acc:
            return helper(idx + 1, tokens, [sorted_token])
        else:
            return helper(idx + 1, tokens, acc + [sorted_token])

    split_tokens: List[str] = []
    temp_str = input_string
    while True:
        space_pos = temp_str.find(" ")
        if space_pos == -1:
            if temp_str:
                split_tokens.append(temp_str)
            break
        split_tokens.append(temp_str[:space_pos])
        temp_str = temp_str[space_pos + 1 :]

    sorted_tokens = helper(0, split_tokens, [])
    output = ""
    for i in range(len(sorted_tokens)):
        if i > 0:
            output += " "
        output += sorted_tokens[i]

    return output