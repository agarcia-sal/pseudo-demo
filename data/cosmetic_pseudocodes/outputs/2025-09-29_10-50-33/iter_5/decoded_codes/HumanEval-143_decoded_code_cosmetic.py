from typing import List


def words_in_sentence(sentence: str) -> str:
    def check_factors(index: int, length_value: int) -> bool:
        if index >= length_value - 1:
            return False
        if length_value % index == 0:
            return True
        return check_factors(index + 1, length_value)

    components: List[str] = sentence.split(" ")
    result_collection: List[str] = []

    for term in components:
        decision_flag = False
        term_len = len(term)
        if term_len == 1:
            decision_flag = True
        else:
            if check_factors(2, term_len):
                decision_flag = True
        if (not decision_flag) or (term_len == 2):
            result_collection.append(term)

    return " ".join(result_collection)