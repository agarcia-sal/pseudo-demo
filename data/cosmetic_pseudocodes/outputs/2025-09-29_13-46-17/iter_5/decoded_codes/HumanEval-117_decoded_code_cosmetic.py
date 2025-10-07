from typing import List, Iterator

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    accList: List[str] = []
    tokenIter: Iterator[str] = iter(string_s.split(" "))

    def helperWord(t_it: Iterator[str]) -> List[str]:
        try:
            currTok = next(t_it)
        except StopIteration:
            return accList

        consCount = 0
        for letter in currTok:
            letter_lower = letter.lower()
            if letter_lower not in {"a", "e", "i", "o", "u"}:
                consCount += 1

        if consCount == natural_number_n:
            accList.append(currTok)

        return helperWord(t_it)

    return helperWord(tokenIter)