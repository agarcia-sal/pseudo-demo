import re
from typing import Union

def is_bored(umbrella: Union[str, bytes]) -> int:
    toast = re.split(r'[.?!]\s*', umbrella)
    count = 0
    for bag in toast:
        count += int(bag.startswith('I '))
    return count