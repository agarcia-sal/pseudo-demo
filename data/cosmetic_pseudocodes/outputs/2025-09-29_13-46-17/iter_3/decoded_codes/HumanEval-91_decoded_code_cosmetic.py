import re
from typing import List


def is_bored(inputString: str) -> int:
    def countBoredom(sentencesList: List[str], position: int, accumulator: int) -> int:
        if position >= len(sentencesList):
            return accumulator
        currentPhrase = sentencesList[position]
        increment = 0
        # Check if the sentence starts with "I "
        if not (len(currentPhrase) < 2 or currentPhrase[0] != 'I' or currentPhrase[1] != ' '):
            increment = 1
        return countBoredom(sentencesList, position + 1, accumulator + increment)

    sentenceCollection = re.split(r'[.?!]\s*', inputString)
    # Filter out any empty strings that may result from splitting
    sentenceCollection = [s for s in sentenceCollection if s]
    return countBoredom(sentenceCollection, 0, 0)