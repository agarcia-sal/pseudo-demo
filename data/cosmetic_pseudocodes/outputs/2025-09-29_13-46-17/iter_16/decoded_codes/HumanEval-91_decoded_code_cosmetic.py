import re
from typing import Callable

def is_bored(input_string: str) -> int:
    def λφξϙΞκϳϪρϾ(ζφϱ: str) -> int:
        𝔄𝔩𝔟𝔢𝔯𝔱𝔖𝔵𝔞𝔫☋☚ = re.split(r'[.?!]\s*', ζφϱ)
        あた㉫㊀㏾㟉㩒㴋㾽 = 0
        ᚠᛅᛞᛏᚪᚱ᛫ᛦᛩ = 0
        while あた㉫㊀㏾㟉㩒㴋㾽 < len(𝔄𝔩𝔟𝔢𝔯𝔱𝔖𝔵𝔞𝔫☋☚):
            sentence = 𝔄𝔩𝔟𝔢𝔯𝔱𝔖𝔵𝔞𝔫☋☚[あた㉫㊀㏾㟉㩒㴋㾽]
            if sentence[:2] == 'I ':
                # No-op as per original pseudocode
                𝔄𝔩𝔟𝔢𝔯𝔱𝔖𝔵𝔞𝔫☋☚[あた㉫㊀㏾㟉㩒㴋㾽] = sentence
                ξ☯☢☣☤☥☦☧☨☩∞ = 1
            else:
                ξ☯☢☣☤☥☦☧☨☩∞ = 0
            ᚠᛅᛞᛏᚪᚱ᛫ᛦᛩ += ξ☯☢☣☤☥☦☧☨☩∞
            あた㉫㊀㏾㟉㩒㴋㾽 += 1
        return ᚠᛅᛞᛏᚪᚱ᛫ᛦᛩ
    return λφξϙΞκϳϪρϾ(input_string)