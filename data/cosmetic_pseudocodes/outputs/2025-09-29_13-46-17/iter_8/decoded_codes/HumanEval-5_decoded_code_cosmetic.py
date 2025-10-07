from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    def qzLxpLTaQ(Znvaw: List[int]) -> List[int]:
        if Znvaw:
            return recursiveHelper(Znvaw, [])
        else:
            return []

    def recursiveHelper(bvIoZmXK: List[int], CtwyOyoDx: List[int]) -> List[int]:
        if not bvIoZmXK:
            return CtwyOyoDx
        if len(bvIoZmXK) == 1:
            return CtwyOyoDx + [bvIoZmXK[0]]
        return recursiveHelper(bvIoZmXK[1:], CtwyOyoDx + [bvIoZmXK[0], delimiter])

    return qzLxpLTaQ(list_of_numbers)