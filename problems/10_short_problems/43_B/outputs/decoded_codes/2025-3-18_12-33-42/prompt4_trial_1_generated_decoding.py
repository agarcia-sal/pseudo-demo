def remove_spaces(s):
    """Removes spaces from the input string."""
    return s.replace(" ", "")

def get_user_input():
    """Gets user input."""
    return input()

def main():
    # Read input strings while removing spaces
    string1 = remove_spaces(get_user_input())
    string2 = remove_spaces(get_user_input())

    # Initialize frequency differences array
    frequency_differences = [0] * 58  # 58 for range A-Z (65-90) and a-z (97-122)

    # Calculate frequency differences for each character from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):  # ASCII values from 'A' to 'z'
        char = chr(char_code)  # Convert ASCII value to character
        count_in_string1 = string1.count(char)
        count_in_string2 = string2.count(char)
        frequency_differences[char_code - 65] = count_in_string1 - count_in_string2

    # Check if all frequency differences are non-negative
    if all(count >= 0 for count in frequency_differences):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
