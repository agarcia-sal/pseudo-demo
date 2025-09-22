def main():
    # Get two lines of input, each representing a string
    string1 = input()
    string2 = input()

    # Process the input strings to remove spaces and store them in lists
    string1_processed = [character for character in string1 if character != ' ']
    string2_processed = [character for character in string2 if character != ' ']

    # Initialize a list to keep track of frequency differences
    frequency_differences = []

    # Calculate the difference in character frequencies between the two strings
    for character_code in range(ord('A'), ord('z') + 1):
        frequency_in_string1 = string1_processed.count(chr(character_code))
        frequency_in_string2 = string2_processed.count(chr(character_code))
        difference = frequency_in_string1 - frequency_in_string2
        frequency_differences.append(difference)

    # Check if there are any negative frequency differences
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
