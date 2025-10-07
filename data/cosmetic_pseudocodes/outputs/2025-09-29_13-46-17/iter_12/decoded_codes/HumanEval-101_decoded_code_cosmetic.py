from typing import List


def words_string(input_string: str) -> List[str]:
    # Split the input string by whitespace and filter out empty strings
    return [word for word in input_string.split() if word]