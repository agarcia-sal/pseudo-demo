from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def analyze(text: str) -> int:
        count_upper = 0
        count_lower = 0
        for ch in text:
            if not ch.islower():
                if ch.isupper():
                    count_upper += 1
            else:
                count_lower += 1
        return count_upper - count_lower

    prime_candidate = extensions[0] if extensions else ""
    max_strength = analyze(prime_candidate) if prime_candidate else float('-inf')

    for current_candidate in extensions:
        candidate_val = analyze(current_candidate)
        if candidate_val > max_strength:
            max_strength = candidate_val
            prime_candidate = current_candidate

    return f"{class_name}.{prime_candidate}"