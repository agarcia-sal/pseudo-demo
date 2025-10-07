from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    filtered_list = [""]
    index = 0
    while index < len(strings):
        current_string = strings[index]
        prefix_length = len(prefix)
        if len(current_string) >= prefix_length:
            substring = ""
            char_index = 0
            while char_index < prefix_length:
                substring += current_string[char_index]
                char_index += 1
            if substring == prefix:
                filtered_list.append(current_string)
        index += 1
    return filtered_list