from collections import deque

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    num_list: deque[int] = deque()
    idx: int = 0
    length: int = len(string_description)

    while idx < length:
        word = ""
        while idx < length and string_description[idx] != " ":
            word += string_description[idx]
            idx += 1
        if word.isdigit():
            num_list.append(int(word))
        idx += 1  # skip the space

    total_sum = 0
    while num_list:
        val = num_list.popleft()
        total_sum += val

    return total_number_of_fruits - total_sum