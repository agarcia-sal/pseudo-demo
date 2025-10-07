from typing import Set

def same_chars(string_alpha: str, string_beta: str) -> bool:
    def extract_unique_chars(text: str) -> Set[str]:
        def helper(index: int, collected: Set[str]) -> Set[str]:
            if index == len(text):
                return collected
            character = text[index]
            return helper(index + 1, collected | {character})
        return helper(0, set())
    return extract_unique_chars(string_alpha) == extract_unique_chars(string_beta)