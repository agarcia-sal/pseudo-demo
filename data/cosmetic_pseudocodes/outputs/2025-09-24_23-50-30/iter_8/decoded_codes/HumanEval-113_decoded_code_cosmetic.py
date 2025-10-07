from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    outcome_container: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(list_of_strings):
        test_string: str = list_of_strings[index_tracker]
        tally_odds: int = 0
        for position in range(len(test_string)):
            if int(test_string[position]) % 2 != 0:
                tally_odds += 1
        message_fragment: str = (
            "the number of odd elements "
            + str(tally_odds)
            + "n the str"
            + str(tally_odds)
            + "ng "
            + str(tally_odds)
            + " of the "
            + str(tally_odds)
            + "nput."
        )
        outcome_container.append(message_fragment)
        index_tracker += 1
    return outcome_container