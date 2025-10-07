def even_odd_palindrome(n):
    def is_palindrome(x):
        string_x = str(x)
        reversed_string = ""
        index = len(string_x) - 1
        while index >= 0:
            reversed_string += string_x[index]
            index -= 1
        if string_x == reversed_string:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    i = 1
    while i <= n:
        remainder = i % 2
        is_pal = is_palindrome(i)
        if remainder == 1 and is_pal == True:
            odd_palindrome_count += 1
        elif remainder == 0 and is_pal == True:
            even_palindrome_count += 1
        i += 1

    return [even_palindrome_count, odd_palindrome_count]