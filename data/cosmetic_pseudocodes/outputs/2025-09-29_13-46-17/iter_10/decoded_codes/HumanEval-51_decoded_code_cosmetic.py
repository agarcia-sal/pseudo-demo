from typing import Callable


def remove_vowels(text: str) -> str:
    def ƛφ𝞪(𝓧℉: str, 𝔳𝓔𝓧𝔱𝔄𝔁: str, 𝜕𝓪𝔙𝓅𝔁: str) -> str:
        if not 𝜕𝓪𝔙𝓅𝔁:
            return 𝓧℉
        𝑳𝓲𝔍𝙚, 𝓟𝒌𝔅𝔁 = 𝜕𝓪𝔙𝓅𝔁[0], 𝜕𝓪𝔙𝓅𝔁[1:]
        if 𝑳𝓲𝔍𝙚 not in {"a", "e", "i", "o", "u"}:
            return ƛφ𝞪(𝓧℉ + 𝑳𝓲𝔍𝙚, 𝔳𝓔𝓧𝔱𝔄𝔁, 𝓟𝒌𝔅𝔁)
        else:
            return ƛφ𝞪(𝓧℉, 𝔳𝓔𝓧𝔱𝔄𝔁, 𝓟𝒌𝔅𝔁)

    return ƛφ𝞪("", text, text)