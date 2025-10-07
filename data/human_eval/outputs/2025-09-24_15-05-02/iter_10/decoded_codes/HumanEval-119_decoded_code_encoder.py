def match_parens(list_of_two_strings):
    def check(string_s):
        val = 0
        for char in string_s:
            if char == '(':
                val += 1
            else:
                val -= 1
            if val < 0:
                return False
        return val == 0

    s1 = list_of_two_strings[0] + list_of_two_strings[1]
    s2 = list_of_two_strings[1] + list_of_two_strings[0]

    if check(s1) or check(s2):
        return 'Yes'
    return 'No'