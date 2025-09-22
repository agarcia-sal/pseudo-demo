def main():
    # Get user input for both strings
    first_string = input()
    second_string = input()

    # Prepare strings by removing spaces
    cleaned_first_string = ''.join(first_string.split())
    cleaned_second_string = ''.join(second_string.split())

    # Initialize a frequency list for character counts (26 + 26 = 52)
    character_frequency = [0] * 52

    # Count characters in cleaned_first_string
    for char in cleaned_first_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26
        else:
            continue
        character_frequency[index] += 1

    # Count characters in cleaned_second_string
    for char in cleaned_second_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26
        else:
            continue
        character_frequency[index] -= 1

    # Check if all character counts are non-negative
    is_sufficient = True
    for count in character_frequency:
        if count < 0:
            is_sufficient = False
            break

    # Output result
    if is_sufficient:
        print("YES")
    else:
        print("NO")

# Entry point of the Python script
if __name__ == "__main__":
    main()
