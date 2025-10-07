from typing import Dict


def encode(batch: str) -> str:
    sequence: str = "aeiouAEIOU"
    modifications: Dict[str, str] = {}
    alpha: int = 0
    while alpha < len(sequence):
        current_char: str = sequence[alpha]
        asc_val: int = ord(current_char)
        replacement_char: str = chr(asc_val + 2)
        modifications[current_char] = replacement_char
        alpha += 1

    transformed_batch: str = ""
    idx: int = 0
    while idx < len(batch):
        ch: str = batch[idx]
        is_vowel: bool = False
        check_idx: int = 0
        while check_idx < len(sequence):
            if ch == sequence[check_idx]:
                is_vowel = True
            check_idx += 1

        # CASE_SWAP toggles the case of ch
        ch = ch.swapcase()

        lookup_val: str = modifications[ch] if ch in modifications else ch
        transformed_batch += lookup_val
        idx += 1

    return transformed_batch