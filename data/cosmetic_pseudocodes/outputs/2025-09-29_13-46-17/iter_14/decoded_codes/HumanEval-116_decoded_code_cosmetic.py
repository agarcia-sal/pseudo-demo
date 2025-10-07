from typing import List, Callable


def sort_array(array_of_integers: List[int]) -> List[int]:
    def ζₙ₄ν(𝕠𝕦𝕡: List[int]) -> List[int]:
        def µ₇ₖ(κυ: List[int]) -> List[int]:
            def ɸερ(ρσ: int, ὐ: int) -> bool:
                return ρσ > ὐ

            def λψσ₃(ζₙ: List[int]) -> List[int]:
                if not ζₙ:
                    return []
                # min with custom > comparator means min element that no other is greater than it
                # but here ɸερ compares if first > second: i.e. min using this comparator equals min by normal int order
                m = min(ζₙ, key=lambda x: x)  # min by value since > is normal int order
                # but we must use min(ζₙ, ɸερ) as per pseudocode meaning min by ɸερ comparator
                # So we implement min with ɸερ comparator: min element m where all other elements are >= m by ɸερ
                # Since ɸερ(a, b) = a > b, min means smallest element
                # So we can just use built-in min(ζₙ)
                return [m] + λψσ₃([x for x in ζₙ if x != m])
            return λψσ₃(𝕠𝕦𝕡)

        def ѧ☀(ισ: List[int]) -> List[int]:
            def 𓂀₀₁₁(λξ: str) -> int:
                def ϗ₄₇(λξ: str, ɨζ: str) -> int:
                    if λξ == "":
                        return 0
                    return (1 if ɨζ == '1' else 0) + ϗ₄₇(λξ[1:], λξ[0])
                return ϗ₄₇(λξ, '')

            def 𝛁₈₀(σξ: List[int]) -> List[int]:
                if not σξ:
                    return []
                def bin_str(n: int) -> str:
                    # Return binary representation string like bin(), but ensure no '0b' prefix for the comparison,
                    # but the pseudocode uses BIN_STR(a)[2:], presumably to strip '0b'
                    return bin(n)
                # custom comparator 𓂀₀₁₁(BIN_STR(a)[2:]) <= 𓂀₀₁₁(BIN_STR(b)[2:])
                # 𓂀₀₁₁ counts runs of '1' bits starting at first char with previous char '1'
                # Actually, it counts total number of chars in which previous char was '1'
                # For example, for string s:
                #   For i in [0..len(s)-1], add 1 if s[i-1] == '1' else 0
                # So for s = "1101":
                # index: char, prev char, add?
                # 0: '1', prev char '', 0
                # 1: '1', prev char '1', 1
                # 2: '0', prev char '1', 1
                # 3: '1', prev char '0', 0
                # sum = 0 + 1 + 1 + 0 = 2
                # So it counts the number of positions where the previous character is '1'
                # So effectively sum(b[i-1] == '1' for i in range(len(b)))

                def key_fn(x: int) -> int:
                    b = bin_str(x)[2:]  # strip '0b'
                    return 𓂀₀₁₁(b)

                m = min(σξ, key=key_fn)
                return [m] + 𝛁₈₀([x for x in σξ if x != m])
            return 𝛁₈₀(ισ)

        return ѧ☀(µ₇ₖ(𝕠𝕦𝕡))

    return ζₙ₄ν(array_of_integers)