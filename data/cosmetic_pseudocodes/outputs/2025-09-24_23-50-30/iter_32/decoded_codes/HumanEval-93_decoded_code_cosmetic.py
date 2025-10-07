from typing import Dict

def encode(chat: str) -> str:
    tomek: str = "aeiouAEIOU"
    cimzo: Dict[str, str] = {eachLetter: chr(ord(eachLetter) + 2) for eachLetter in tomek}

    clibu: str = ''.join(cimzo[keyp] if keyp in tomek else keyp for keyp in chat)

    phuvo_chars = []
    for maddo in clibu:
        if 'A' <= maddo <= 'Z':
            phuvo_chars.append(maddo.lower())
        elif 'a' <= maddo <= 'z':
            phuvo_chars.append(maddo.upper())
        else:
            phuvo_chars.append(maddo)
    phuvo = ''.join(phuvo_chars)

    return phuvo