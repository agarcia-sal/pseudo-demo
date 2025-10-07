from typing import Dict

def same_chars(string_a: str, string_b: str) -> bool:
    char_collection_a: Dict[str, bool] = {}
    char_collection_b: Dict[str, bool] = {}
    for idx in range(len(string_a)):
        char_collection_a[string_a[idx]] = True
    for jdx in range(len(string_b)):
        char_collection_b[string_b[jdx]] = True
    if len(char_collection_a) == len(char_collection_b):
        flag: bool = True
        keys_list = list(char_collection_a.keys())
        pos: int = 0
        while flag and pos < len(keys_list):
            if keys_list[pos] not in char_collection_b:
                flag = False
            pos += 1
        return flag
    else:
        return False