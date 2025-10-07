from typing import Dict

def encode(input_text: str) -> str:
    alpha_set = "AEIOUaeiou"
    mapping: Dict[str, str] = {char: chr(ord(char) + 2) for char in alpha_set}
    toggled_text = ''.join(c.lower() if c.isupper() else c.upper() for c in input_text)
    output_list = [mapping[symbol] if symbol in alpha_set else symbol for symbol in toggled_text]
    return ''.join(output_list)