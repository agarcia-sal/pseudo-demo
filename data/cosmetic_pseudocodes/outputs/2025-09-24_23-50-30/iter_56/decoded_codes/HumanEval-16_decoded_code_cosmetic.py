def count_distinct_characters(hypervariable: str) -> int:
    return len({char_var for char_var in hypervariable.lower()})