def main():
    # Read two input strings from the user
    input_string1 = input()
    input_string2 = input()

    # Remove spaces from both input strings
    cleaned_string1 = input_string1.replace(" ", "")
    cleaned_string2 = input_string2.replace(" ", "")

    # Initialize a frequency list to track the count difference of each character (ASCII range)
    frequency_difference = [0] * 128  # There are 128 standard ASCII characters

    # Calculate frequency difference for each character from 'A' to 'z'
    for character_code in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
        count_in_string1 = cleaned_string1.count(chr(character_code))
        count_in_string2 = cleaned_string2.count(chr(character_code))
        frequency_difference[character_code] = count_in_string1 - count_in_string2

    # Check if all frequency differences are non-negative
    if all(count >= 0 for count in frequency_difference[65:123]):  # Focus on relevant range
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
