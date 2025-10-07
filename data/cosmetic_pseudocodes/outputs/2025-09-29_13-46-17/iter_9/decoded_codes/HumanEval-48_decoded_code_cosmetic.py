from typing import Callable

def is_palindrome(𝒙ᛉ: str) -> bool:
    def 𝔄ᾮ(𝚿: str, 𝛕: int, 𝜜: int) -> bool:
        if not (𝛕 < 𝜜):
            return True
        if 𝚿[𝛕] != 𝚿[len(𝚿) - 1 - 𝛕]:
            return False
        return 𝔄ᾮ(𝚿, 𝛕 + 1, 𝜜)
    return 𝔄ᾮ(𝒙ᛉ, 0, len(𝒙ᛉ))