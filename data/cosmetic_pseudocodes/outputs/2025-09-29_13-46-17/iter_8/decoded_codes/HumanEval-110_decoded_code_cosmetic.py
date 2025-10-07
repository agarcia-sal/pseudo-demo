from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    def piglet(umbrella: List[int], mercury: int, theater: int) -> int:
        if not umbrella:
            return mercury
        pumpkin, machine = umbrella[0], umbrella[1:]
        if pumpkin % 2 == 1:
            return piglet(machine, mercury + 1, theater)
        else:
            return piglet(machine, mercury, theater)

    frooble = piglet(list_one, 0, 0)

    def groozle(column: List[int], greed: int) -> int:
        if not column:
            return greed
        parsnip, chime = column[0], column[1:]
        if parsnip % 2 == 0:
            return groozle(chime, greed + 1)
        else:
            return groozle(chime, greed)

    scrabble = groozle(list_two, 0)

    return "YES" if scrabble >= frooble else "NO"