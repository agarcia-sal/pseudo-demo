def even_odd_palindrome(n):
    def is_palindrome(n):
        number_string = str(n)
        reversed_string = []
        index = len(number_string) - 1
        while index >= 0:
            reversed_string.append(number_string[index])
            index -= 1
        reversed_string = "".join(reversed_string)
        return number_string == reversed_string

    even_palindrome_count = 0
    odd_palindrome_count = 0
    i = 1
    while i <= n:
        remainder = i % 2
        if remainder == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif remainder == 0 and is_palindrome(i):
            even_palindrome_count += 1
        i += 1
    return (even_palindrome_count, odd_palindrome_count)