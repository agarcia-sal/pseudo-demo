def fix_spaces(text: str) -> str:
    new_text = []
    start = 0
    end = 0
    index = 0

    while index < len(text):
        char = text[index]
        if char == " ":
            end += 1
        else:
            gap = end - start
            if gap > 2:
                new_text.append("-")
                new_text.append(char)
            elif gap > 0:
                new_text.append("_" * gap)
                new_text.append(char)
            else:
                new_text.append(char)
            start = index + 1
            end = index + 1
        index += 1

    remainder = end - start
    if remainder > 2:
        new_text.append("-")
    elif remainder > 0:
        new_text.append("_")

    return "".join(new_text)