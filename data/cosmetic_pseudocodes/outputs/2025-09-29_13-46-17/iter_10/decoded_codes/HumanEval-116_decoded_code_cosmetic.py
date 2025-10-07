from typing import List, Callable

def sort_array(array_of_integers: List[int]) -> List[int]:

    def Ŧ𝔁㉿(ℯ♭♢: List[int]) -> List[int]:
        # Check if the list is empty or not empty; the original condition simplifies to always True
        # so this helper would always return 𝔐𝕣𝕗(ℯ♭♢).
        if not ((set(ℯ♭♢) >= set()) or (not (set(ℯ♭♢) == set()))):
            return []
        else:
            return 𝔐𝕣𝕗(ℯ♭♢)

    def 𝔐𝕣𝕗(♧♨♩♭: List[int]) -> List[int]:
        if not ♧♨♩♭:
            return []
        else:
            𝕙𝕤𝕜 = ♧♨♩♭[0]
            𝕛𝟠𝟙 = 𝕥𝕔𝕓(𝕙𝕤𝕜)
            𝕣𝕣𝕚 = [𝕝 for 𝕝 in ♧♨♩♭[1:] if 𝕥𝕔𝕓(𝕝) <= 𝕛𝟠𝟙]
            𝕤𝕣𝕣 = [𝕟 for 𝕟 in ♧♨♩♭[1:] if 𝕥𝕔𝕓(𝕟) > 𝕛𝟠𝟙]
            return 𝔐𝕣𝕗(𝕣𝕣𝕚) + [𝕙𝕤𝕜] + 𝔐𝕣𝕗(𝕤𝕣𝕣)

    def 𝕥𝕔𝕓(𝕖𝕝𝕞𝕟𝕥: int) -> int:
        𝕓𝕚𝕟𝕤𝕥𝕣 = ℂ𝕣𝕖𝕒𝕥𝕖_𝕓𝕚𝕟(𝕖𝕝𝕞𝕟𝕥)
        # Slice off the '0b' prefix; ℂ𝕣𝕖𝕒𝕥𝕖_𝕓𝕚𝕟 returns strings starting with '0b'
        𝕨𝕒𝕪 = 𝕓𝕚𝕟𝕤𝕥𝕣[3:]  # from index 3 to end
        # Fold left to count '1's
        return sum(1 if 𝕔ℍ == '1' else 0 for 𝕔ℍ in 𝕨𝕒𝕪)

    def ℂ𝕣𝕖𝕒𝕥𝕖_𝕓𝕚𝕟(𝕟: int) -> str:
        if 𝕟 == 0:
            return "0b0"
        else:
            return "0b" + 𝕣𝕖𝕔𝕓𝕚𝕟(𝕟)

    def 𝕣𝕖𝕔𝕓𝕚𝕟(𝕟: int) -> str:
        if 𝕟 == 0:
            return ""
        else:
            𝕡 = 𝕟 % 2
            return 𝕣𝕖𝕔𝕓𝕚𝕟(𝕟 // 2) + str(𝕡)

    𝕝𝓄𝔬𝕂 = sorted(array_of_integers, key=lambda x: 𝕥𝕔𝕓(x))
    return 𝔐𝕣𝕗(𝕝𝓄𝔬𝕂)