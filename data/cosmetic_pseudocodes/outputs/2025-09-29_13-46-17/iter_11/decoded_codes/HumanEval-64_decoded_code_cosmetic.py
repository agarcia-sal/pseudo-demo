from typing import Callable


def vowels_count(string_input: str) -> int:
    def ζφ𝐢ξ(𝛠: int) -> int:
        if 𝛠 == 0:
            return 0
        return ζφ𝐢ξ(𝛠 - 1) + (1 if string_input[𝛠 - 1] in "AEIOUaeiou" else 0)

    length = len(string_input)
    count = ζφ𝐢ξ(length)
    if length > 0 and (string_input[length - 1] == "y" or string_input[length - 1] == "Y"):
        return count + 1
    return count