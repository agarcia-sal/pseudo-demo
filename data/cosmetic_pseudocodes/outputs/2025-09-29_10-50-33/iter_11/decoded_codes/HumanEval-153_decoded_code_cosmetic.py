from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> object:
    best_candidate: str = extensions[0]
    best_score: int = sum(1 for c in best_candidate if 'A' <= c <= 'Z') - sum(1 for c in best_candidate if 'a' <= c <= 'z')

    i: int = 0
    while i < len(extensions):
        current_entry: str = extensions[i]
        upper_count: int = 0
        lower_count: int = 0
        j: int = 0

        while True:
            if j >= len(current_entry):
                break
            c = current_entry[j]
            if 'A' <= c <= 'Z':
                upper_count += 1
            elif 'a' <= c <= 'z':
                lower_count += 1
            j += 1

            if j >= len(current_entry):
                break

        current_score: int = upper_count - lower_count

        if current_score > best_score:
            best_candidate = current_entry
            best_score = current_score

        i += 1

    final_result: str = f"{class_name}.{best_candidate}"
    return eval(final_result)