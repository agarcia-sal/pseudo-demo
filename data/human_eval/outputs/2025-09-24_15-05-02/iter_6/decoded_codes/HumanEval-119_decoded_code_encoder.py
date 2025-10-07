def match_parens(list_of_two_strings):
    def check(parentheses_string):
        balance = 0
        for char in parentheses_string:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    concatenation_one = list_of_two_strings[0] + list_of_two_strings[1]
    concatenation_two = list_of_two_strings[1] + list_of_two_strings[0]

    if check(concatenation_one) or check(concatenation_two):
        return 'Yes'
    else:
        return 'No'