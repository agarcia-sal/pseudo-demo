from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {}
    for i in vowels:
        vowels_replace[i] = chr(ord(i) + 2)
    message = message.swapcase()
    result = []
    for i in message:
        if i in vowels:
            result.append(vowels_replace[i])
        else:
            result.append(i)
    return ''.join(result)