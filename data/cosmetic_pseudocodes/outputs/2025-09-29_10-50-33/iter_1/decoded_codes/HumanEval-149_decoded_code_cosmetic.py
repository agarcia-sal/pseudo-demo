from typing import List

def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    list_of_strings.sort()  # Sort strings alphabetically in place
    new_list: List[str] = []
    for index in range(len(list_of_strings)):
        current_string = list_of_strings[index]
        if len(current_string) % 2 == 0:
            new_list.append(current_string)
    new_list.sort(key=len)
    return new_list