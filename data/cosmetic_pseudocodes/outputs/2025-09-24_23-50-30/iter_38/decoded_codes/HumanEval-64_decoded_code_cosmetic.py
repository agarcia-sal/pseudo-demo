def vowels_count(text_param: str) -> int:
    key_collection = "AEIOUaeiou"
    tally = sum(1 for element in text_param if element in key_collection)
    if text_param and text_param[-1] in {'y', 'Y'}:
        tally += 1
    return tally