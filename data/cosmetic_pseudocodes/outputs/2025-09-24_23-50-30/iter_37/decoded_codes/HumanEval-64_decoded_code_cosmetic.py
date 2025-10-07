from functools import reduce

def vowels_count(text_value: str) -> int:
    vowels_collection: str = "AEIOUaeiou"
    total_vowels: int = reduce(
        lambda accumulator, item: accumulator + (1 if item in vowels_collection else 0),
        text_value,
        0,
    )
    if text_value[-1:].lower() == 'y':
        total_vowels += 1
    return total_vowels