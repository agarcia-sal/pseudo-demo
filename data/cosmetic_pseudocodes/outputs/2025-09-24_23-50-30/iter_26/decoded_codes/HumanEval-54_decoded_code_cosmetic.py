from typing import List


def same_chars(string_alpha: str, string_beta: str) -> bool:
    collection_a: List[str] = []
    collection_b: List[str] = []

    for index_x in range(len(string_alpha)):
        if string_alpha[index_x] not in collection_a:
            collection_a.append(string_alpha[index_x])

    for index_y in range(len(string_beta)):
        if string_beta[index_y] not in collection_b:
            collection_b.append(string_beta[index_y])

    if len(collection_a) != len(collection_b):
        return False
    else:
        for element_c in collection_a:
            found_flag = False
            for element_d in collection_b:
                if element_c == element_d:
                    found_flag = True
                    break
            if not found_flag:
                return False
        return True