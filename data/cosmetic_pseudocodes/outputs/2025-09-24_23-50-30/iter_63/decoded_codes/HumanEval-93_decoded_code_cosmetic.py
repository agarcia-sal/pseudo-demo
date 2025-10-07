from typing import Dict

def encode(stringInput: str) -> str:
    swapCaseVowels: str = "aeiouAEIOU"
    shiftByTwoAsc: str = ''.join(chr(ord(c) + 2) for c in swapCaseVowels)
    mappingDict: Dict[str, str] = {swapCaseVowels[i]: shiftByTwoAsc[i] for i in range(len(swapCaseVowels))}
    toggledString: str = ''.join(
        c.lower() if c.isupper() else c.upper() if c.islower() else c
        for c in stringInput
    )
    resultString: str = ''.join(mappingDict.get(ch, ch) for ch in toggledString)
    return resultString