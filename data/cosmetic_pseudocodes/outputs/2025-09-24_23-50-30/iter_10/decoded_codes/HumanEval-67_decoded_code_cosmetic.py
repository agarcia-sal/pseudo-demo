from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def extract_digits(seq: List[str], idx: int, acc: List[int]) -> List[int]:
        if idx == len(seq):
            return acc
        else:
            if seq[idx].isdigit():
                acc = acc + [int(seq[idx])]  # Append digit as int
            return extract_digits(seq, idx + 1, acc)

    tokens: List[str] = string_description.split(' ')
    digits_found: List[int] = extract_digits(tokens, 0, [])
    total_extracted: int = sum(digits_found)
    return total_number_of_fruits - total_extracted