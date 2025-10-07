from typing import Collection, List


def total_match(collection_alpha: Collection[str], collection_beta: Collection[str]) -> Collection[str]:
    sum_alpha: int = sum(len(string_token) for string_token in collection_alpha)
    sum_beta: int = sum(len(string_token) for string_token in collection_beta)
    if not (sum_alpha > sum_beta):
        return collection_alpha
    return collection_beta