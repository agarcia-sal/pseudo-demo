from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        contains_substring = False
        sub_index = 0
        while sub_index <= len(current_string) - len(substring):
            match_found = True
            char_index = 0
            while char_index < len(substring):
                if current_string[sub_index + char_index] != substring[char_index]:
                    match_found = False
                    break
                char_index += 1
            if match_found:
                contains_substring = True
                break
            sub_index += 1
        if contains_substring:
            result.append(current_string)
        index += 1
    return result