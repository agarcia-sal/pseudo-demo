from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    freqs: Dict[str, int] = {}
    chars = input_text.split(" ")
    maxFreq = 0

    idx = 0
    while idx < len(chars):
        curr = chars[idx]
        currCount = chars.count(curr)
        if curr != "" and currCount > maxFreq:
            maxFreq = currCount
        idx += 1

    if 0 < maxFreq:
        j = 0
        while j < len(chars):
            symbol = chars[j]
            symbolCount = chars.count(symbol)
            if symbolCount == maxFreq:
                freqs[symbol] = maxFreq
            j += 1

    return freqs