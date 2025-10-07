def even_odd_palindrome(n):
    def is_palindrome(n):
        string_n = str(n)
        reversed_string_n = ""
        index = len(string_n) - 1
        while index >= 0:
            reversed_string_n += string_n[index]
            index -= 1
        if string_n == reversed_string_n:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0
    i = 1
    while i <= n:
        remainder = i % 2
        palindrome_check = is_palindrome(i)
        if remainder == 1 and palindrome_check == True:
            odd_palindrome_count += 1
        elif remainder == 0 and palindrome_check == True:
            even_palindrome_count += 1
        i += 1

    return [even_palindrome_count, odd_palindrome_count]