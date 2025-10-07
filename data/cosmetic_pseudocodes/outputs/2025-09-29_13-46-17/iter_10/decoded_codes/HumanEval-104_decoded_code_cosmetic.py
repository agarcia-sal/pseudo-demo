from typing import List, Callable


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def Ϙζ₮(ℵ⊙: List[int], ㉿: int, ϝϞ: bool) -> bool:
        if not ϝϞ:
            return False
        if ㉿ == 0:
            return True
        ﻼ = ㉿ % 10
        ﻼ = not (ﻼ % 2 == 0)  # True if digit is odd
        return Ϙζ₮(ℵ⊙, ㉿ // 10, ﻼ and ϝϞ)

    def ɉǂ⧈(Ϡ: List[int], ɽϯ: int, 助: List[int]) -> List[int]:
        if ɽϯ >= len(Ϡ):
            return 助
        ɽϯ↝ = ɽϯ + 1
        ℐ𝜓 = Ϡ[ɽϯ]
        𐊠 = Ϙζ₮(Ϡ, ℐ𝜓, True)
        if 𐊠:
            return ɉǂ⧈(Ϡ, ɽϯ↝, 助 + [ℐ𝜓])
        else:
            return ɉǂ⧈(Ϡ, ɽϯ↝, 助)

    def fold(function: Callable[[bool, bool], bool], iterable: List[bool], initial: bool) -> bool:
        result = initial
        for item in iterable:
            result = function(result, item)
        return result

    def fold_insert(sorted_list: List[int], value: int) -> List[int]:
        # Insert value into sorted_list preserving ascending order
        for i, v in enumerate(sorted_list):
            if value < v:
                return sorted_list[:i] + [value] + sorted_list[i:]
        return sorted_list + [value]

    def י▒ɣ(ἣϺ: List[int]) -> List[int]:
        if not ἣϺ:
            return []
        𝙦 = ἣϺ[0]
        𝙝 = ἣϺ[1:]
        𝐿 = י▒ɣ(𝙝)

        # Check if 𝐿 is strictly ascending
        𝙩 = fold(lambda a, b: a and (b < b), [True] + [𝐿[i] < 𝐿[i + 1] for i in range(len(𝐿) -1)], True) if len(𝐿) > 1 else True
        # Check if 𝐿 is strictly descending
        𝙧 = fold(lambda a, b: a and (b < b), [True] + [𝐿[i] > 𝐿[i + 1] for i in range(len(𝐿) -1)], True) if len(𝐿) > 1 else True

        # But this does not make sense as per pseudocode because fold((a, b) → a < b, L, True) means fold with function (a,b): a<b starting from True across L

        # reinterpret: folding with (a, b) -> a < b over L starting True means checking if all consecutive pairs are ascending?

        # Instead, interpret 𝙩 as checking if L is strictly ascending:
        # 𝙩 = all(𝐿[i] < 𝐿[i+1] for i in range(len(𝐿)-1)) or True if len <=1
        # Similarly 𝙧 is all strictly descending:
        # 𝙧 = all(𝐿[i] > 𝐿[i+1] for i in range(len(𝐿)-1)) or True if len<=1

        if len(𝐿) <= 1:
            𝙩 = True
            𝙧 = True
        else:
            𝙩 = all(𝐿[i] < 𝐿[i + 1] for i in range(len(𝐿) - 1))
            𝙧 = all(𝐿[i] > 𝐿[i + 1] for i in range(len(𝐿) - 1))

        if not (𝙩 and 𝙧):
            return fold_insert(𝐿, 𝙦)
        else:
            return [𝙦] + 𝐿

    ▼ȷ↝ = ɉǂ⧈(list_of_positive_integers, 0, [])
    𒅈 = י▒ɣ(▼ȷ↝)
    return 𒅈