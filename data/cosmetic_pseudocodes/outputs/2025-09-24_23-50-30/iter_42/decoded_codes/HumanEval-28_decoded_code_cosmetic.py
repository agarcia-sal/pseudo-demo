from collections.abc import Iterable

def concatenate(collection_of_texts: Iterable[str]) -> str:
    target: str = ""
    index: int = 0
    limit: int = len(collection_of_texts)  # type: ignore
    while index < limit:
        target += collection_of_texts[index]  # type: ignore
        index += 1
    return target