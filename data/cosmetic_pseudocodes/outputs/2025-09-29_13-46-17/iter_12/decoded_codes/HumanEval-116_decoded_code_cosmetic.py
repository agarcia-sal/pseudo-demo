from typing import List

def sort_array(ϺȿӞ: List[int]) -> List[int]:
    def Insert_In_Order(lst: List[int], val: int) -> List[int]:
        if not lst:
            return [val]
        if val <= lst[0]:
            return [val] + lst
        return [lst[0]] + Insert_In_Order(lst[1:], val)

    def BinaryString(⨕: int) -> str:
        if ⨕ == 0:
            return "0"
        𝞵 = ""
        𝛔 = ⨕
        while 𝛔 > 0:
            𝞵 = str(𝛔 % 2) + 𝞵
            𝛔 //= 2
        return 𝞵

    def Count(c: str, s: str) -> int:
        def 𝞂(ρ: int, ὤ: str) -> int:
            if not ὤ:
                return ρ
            return 𝞂(ρ + (1 if ὤ[0] == c else 0), ὤ[1:])
        return 𝞂(0, s)

    𝛂𝠙: List[int] = (lambda ȼκ: (lambda ℧: ℧([], ȼκ, 0))(
        # ℧(nest, seq, idx)
        lambda nest, seq, idx: nest if idx >= len(seq) else __import__('__main__').sort_array.__closure__[0].cell_contents.Insert_In_Order(nest, seq[idx]) if False else __import__('__main__').sort_array.__closure__[0].cell_contents.BinaryString(0) or (
            lambda ℧_: ℧_(Insert_In_Order(nest, seq[idx]), seq, idx+1)
        )(0)
    ))(ϺȿӞ)
    # Since the above tries to inline a recursion using undefined inline, we'll rewrite explicitly:

    def ℧(nest: List[int], seq: List[int], idx: int) -> List[int]:
        if idx >= len(seq):
            return nest
        return ℧(Insert_In_Order(nest, seq[idx]), seq, idx + 1)

    𝛂𝠙 = ℧([], ϺȿӞ, 0)

    def 𝙓𝓋(府: int, ℓ𝕨: List[int]) -> List[int]:
        length = len(ℓ𝕨)
        if length == 0:
            return []
        if length == 1:
            return ℓ𝕨
        first_partition = [x for x in ℓ𝕨 if Count('1', BinaryString(x)) == 府]
        if 府 == length:
            rest_partition = []
        else:
            rest_partition = 𝙓𝓋(府 + 1, ℓ𝕨)
        return first_partition + rest_partition

    return 𝙓𝓋(0, 𝛂𝠙)


def BinaryString(⨕: int) -> str:
    if ⨕ == 0:
        return "0"
    𝞵 = ""
    𝛔 = ⨕
    while 𝛔 > 0:
        𝞵 = str(𝛔 % 2) + 𝞵
        𝛔 //= 2
    return 𝞵


def Count(c: str, s: str) -> int:
    def 𝞂(ρ: int, ὤ: str) -> int:
        if not ὤ:
            return ρ
        return 𝞂(ρ + (1 if ὤ[0] == c else 0), ὤ[1:])
    return 𝞂(0, s)


def Insert_In_Order(lst: List[int], val: int) -> List[int]:
    if not lst:
        return [val]
    if val <= lst[0]:
        return [val] + lst
    return [lst[0]] + Insert_In_Order(lst[1:], val)