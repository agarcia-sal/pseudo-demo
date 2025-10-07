from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def λ𝗥ₔ(🝕𝙹𝙺: str) -> bool:
        length = len(🝕𝙹𝙺)
        for i in range(length // 2):
            if 🝕𝙹𝙺[i] != 🝕𝙹𝙺[length - i - 1]:
                return False
        return True
    return λ𝗥ₔ(input_string)


def make_palindrome(input_string: str) -> str:
    𝙧𝝚𝝗𝝫 = (input_string == "")
    if 𝙧𝝚𝝗𝝫:
        return ""

    ʭᔑꙪ = 0

    def ᔚ🐚(𝤤𝓀: int) -> int:
        nonlocal ʭᔑꙪ
        if 𝤤𝓀 >= len(input_string):
            return ʭᔑꙪ
        🙊ݨ = input_string[𝤤𝓀:]
        ᴚ𝗍Ꭵ𝗠𝗚𝓪𝓎𝓰𝟭𝟯𝟷𝕽 = is_palindrome(🙊ݨ)
        if not ᴚ𝗍Ꭵ𝗠𝗚𝓪𝓎𝓰𝟭𝟯𝟷𝕽:
            ʭᔑꙪ = 𝤤𝓀 + 1
            return ᔚ🐚(𝤤𝓀 + 1)
        else:
            return 𝤤𝓀

    🧞 = ᔚ🐚(0)
    𝟙෴ = input_string[:🧞]
    𝟡🧛 = "".join(reversed(𝟙෴))
    return input_string + 𝟡🧛