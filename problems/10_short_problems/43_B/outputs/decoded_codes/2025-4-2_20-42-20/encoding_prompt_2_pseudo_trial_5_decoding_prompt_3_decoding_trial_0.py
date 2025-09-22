def main():
    # Step 1: Get Input
    first_string = input()
    second_string = input()

    # Step 2: Process Input
    processed_first_string = []
    processed_second_string = []

    for char in first_string:
        if char != ' ':
            processed_first_string.append(char)

    for char in second_string:
        if char != ' ':
            processed_second_string.append(char)

    # Step 3: Frequency Calculation
    frequency_differences = []
    
    # Iterate over ASCII values from 'A'(65) to 'z'(122)
    for ascii_code in range(ord('A'), ord('z') + 1):
        # Count occurrences in the processed strings
        count_first = processed_first_string.count(chr(ascii_code))
        count_second = processed_second_string.count(chr(ascii_code))
        # Calculate the frequency difference
        frequency_difference = count_first - count_second
        frequency_differences.append(frequency_difference)

    # Step 4: Condition Check and Output
    if any(diff < 0 for diff in frequency_differences):
        print("NO")
    else:
        print("YES")

# Ensure the function runs when the script is executed
if __name__ == "__main__":
    main()
