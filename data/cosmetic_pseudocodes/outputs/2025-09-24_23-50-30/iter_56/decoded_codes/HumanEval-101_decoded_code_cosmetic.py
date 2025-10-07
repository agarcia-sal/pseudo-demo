from typing import List


def words_string(datum: str) -> List[str]:
    if datum == "":
        return []

    def recombine(ix: int, codex: List[str]) -> List[str]:
        if ix >= len(codex):
            return codex
        # Replace comma at position ix with a space and recurse
        if codex[ix] == ",":
            codex = codex[:ix] + [" "] + codex[ix + 1 :]
        return recombine(ix + 1, codex)

    converted_list = recombine(0, list(datum))
    unified_string = "".join(converted_list)
    # Split on whitespace and filter out empty strings
    return [segment for segment in unified_string.split() if segment != ""]