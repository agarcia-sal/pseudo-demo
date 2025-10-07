def solve(input_D: object) -> str:
    accumulator: int = 0
    chars: str = str(input_D)
    indexer: int = 0
    while indexer < len(chars):
        accumulator += int(chars[indexer])
        indexer += 1
    binary_full: str = bin(accumulator)
    result_str: str = binary_full[2:]
    return result_str