from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def calc_strength(sample: str) -> int:
        upper_count = 0
        lower_count = 0
        for ch in sample:
            if 'A' <= ch <= 'Z':
                upper_count += 1
            elif 'a' <= ch <= 'z':
                lower_count += 1
        return upper_count - lower_count

    def find_strongest(current_best: str, remaining_extensions: List[str], current_max: int) -> str:
        if not remaining_extensions:
            return current_best
        candidate = remaining_extensions[0]
        candidate_val = calc_strength(candidate)
        if candidate_val > current_max:
            return find_strongest(candidate, remaining_extensions[1:], candidate_val)
        else:
            return find_strongest(current_best, remaining_extensions[1:], current_max)

    initial_extension = extensions[0]
    initial_strength = calc_strength(initial_extension)
    strongest_name = find_strongest(initial_extension, extensions[1:], initial_strength)
    return f"{class_name}.{strongest_name}"