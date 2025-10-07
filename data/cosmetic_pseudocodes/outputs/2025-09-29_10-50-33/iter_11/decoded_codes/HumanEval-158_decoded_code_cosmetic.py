from typing import List

def find_max(collection_of_terms: List[str]) -> str:
    n = len(collection_of_terms)
    # Sort collection_of_terms in place according to the pseudocode logic
    for idx in range(n - 1):
        for jdx in range(idx + 1, n):
            unique_chars_a = len(set(collection_of_terms[idx]))
            unique_chars_b = len(set(collection_of_terms[jdx]))
            if not (unique_chars_a > unique_chars_b):
                if unique_chars_a == unique_chars_b:
                    if collection_of_terms[idx] > collection_of_terms[jdx]:
                        collection_of_terms[idx], collection_of_terms[jdx] = collection_of_terms[jdx], collection_of_terms[idx]
                else:
                    collection_of_terms[idx], collection_of_terms[jdx] = collection_of_terms[jdx], collection_of_terms[idx]
    return collection_of_terms[0]