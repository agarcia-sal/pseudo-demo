def main():
    # Step 1: Read Input
    first_string = input()
    second_string = input()

    # Step 2: Process Input
    cleaned_first_string = ''.join(first_string.split())
    cleaned_second_string = ''.join(second_string.split())

    # Step 3: Initialize Frequency Count
    frequency_difference = [0] * 256  # ASCII range size

    # Step 4: Calculate Frequency Differences
    for char in range(256):  # ASCII characters range
        char_count = cleaned_first_string.count(chr(char)) - cleaned_second_string.count(chr(char))
        frequency_difference[char] = char_count

    # Step 5: Check for Negative Frequencies
    has_negative_frequency = any(count < 0 for count in frequency_difference)

    # Step 6: Output Result
    if not has_negative_frequency:
        print("YES")
    else:
        print("NO")

# Ensure the function runs when this script is executed
if __name__ == "__main__":
    main()
