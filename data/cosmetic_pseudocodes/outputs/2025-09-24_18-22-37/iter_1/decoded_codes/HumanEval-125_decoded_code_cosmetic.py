from typing import List, Union

def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    elif ',' in text:
        temp_text = text.replace(',', ' ')
        return temp_text.split()
    else:
        # Filter characters that are lowercase and have even ASCII value
        filtered = [c for c in text if c.islower() and (ord(c) % 2 == 0)]
        return len(filtered)