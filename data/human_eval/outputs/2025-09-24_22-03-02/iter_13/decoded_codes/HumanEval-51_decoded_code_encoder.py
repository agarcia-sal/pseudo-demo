def remove_vowels(text: str) -> str:
    result_list = []
    for s in text:
        if s.lower() not in ["a", "e", "i", "o", "u"]:
            result_list.append(s)
    result_string = "".join(result_list)
    return result_string