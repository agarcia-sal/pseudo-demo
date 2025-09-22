def main():
    # Step 1: Get Input
    first_string = input().strip()  # Read the first input string
    second_string = input().strip()  # Read the second input string

    # Step 2: Process Input to remove spaces
    processed_first_string = [char for char in first_string if char != ' ']
    processed_second_string = [char for char in second_string if char != ' ']

    # Step 3: Frequency Calculation
    frequency_differences = []
    
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        count_first = processed_first_string.count(char)
        count_second = processed_second_string.count(char)
        difference = count_first - count_second
        frequency_differences.append(difference)

    # Step 4: Condition Check and Output
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
