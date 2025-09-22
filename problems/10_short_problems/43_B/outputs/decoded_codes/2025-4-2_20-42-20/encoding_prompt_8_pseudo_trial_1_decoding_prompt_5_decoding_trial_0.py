def main():
    # Get user input for both strings
    first_string = input()
    second_string = input()
    
    # Remove all spaces from the input strings
    cleaned_first_string = ''.join(first_string.split())
    cleaned_second_string = ''.join(second_string.split())
    
    # Initialize a frequency list for character counts (52 for A-Z and a-z)
    character_frequency = [0] * 52

    # Count characters in the first string
    for char in cleaned_first_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')  # Uppercase letters: A-Z
        else:
            index = ord(char) - ord('a') + 26  # Lowercase letters: a-z
        character_frequency[index] += 1

    # Decrease counts based on characters in the second string
    for char in cleaned_second_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
        else:
            index = ord(char) - ord('a') + 26
        character_frequency[index] -= 1

    # Check if the first string has sufficient characters for the second string
    is_sufficient = True
    for count in character_frequency:
        if count < 0:
            is_sufficient = False
            break

    # Output the result
    if is_sufficient:
        print("YES")
    else:
        print("NO")

# You can call main() to execute the function and test the behavior
