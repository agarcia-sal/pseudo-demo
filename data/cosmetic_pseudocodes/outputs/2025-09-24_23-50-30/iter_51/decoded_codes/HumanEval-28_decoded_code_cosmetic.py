from typing import List


def concatenate(array_of_chunks: List[str]) -> str:
    def gather(index: int, acc: str) -> str:
        if index > len(array_of_chunks):
            return acc
        else:
            return gather(index + 1, acc + array_of_chunks[index - 1])

    return gather(1, "")