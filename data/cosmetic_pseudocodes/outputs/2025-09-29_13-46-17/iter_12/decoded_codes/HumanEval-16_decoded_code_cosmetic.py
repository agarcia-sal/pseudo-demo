from typing import Set

def count_distinct_characters(X𝖰𝕠𝖓: str) -> int:
    def 𝖿(𝖺: str) -> str:
        # Normalize character to lowercase if it's an ASCII letter
        if 'a' <= 𝖺 <= 'z':
            return 𝖺
        if 'A' <= 𝖺 <= 'Z':
            return chr(ord(𝖺) + (ord('a') - ord('A')))
        return 𝖺

    def 𝞔Ꭾﾉ⨳(𝞔: Set[str], 𝝢: int) -> Set[str]:
        return 𝞔 if 𝝢 == 0 else 𝞔Ꭾﾉ⨳(𝞔 | {𝖿(X𝖰𝕠𝖓[𝝢 - 1])}, 𝝢 - 1)

    𝖥𝒖𝑁𝒄𝓁 = 𝞔Ꭾﾉ⨳(set(), len(X𝖰𝕠𝖓))
    Ͷ = len(𝖥𝒖𝑁𝒄𝓁)
    return Ͷ