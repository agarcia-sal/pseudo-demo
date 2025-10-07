from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    symbol_collection: List[str] = []

    def process_index(idx: int) -> None:
        if idx >= len(input_string):
            return
        symbol = input_string[idx]
        if symbol == ",":
            symbol_collection.append(" ")
        else:
            symbol_collection.append(symbol)
        process_index(idx + 1)

    process_index(0)

    combined_text = "".join(symbol_collection)
    return combined_text.split()