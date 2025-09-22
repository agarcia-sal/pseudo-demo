def main():
    # Receive Input
    first_string = input()
    second_string = input()

    # Process Input to Remove Spaces
    processed_first_string = [char for char in first_string if char != ' ']
    processed_second_string = [char for char in second_string if char != ' ']

    # Initialize Frequency Count
    frequency_differences = [0] * (ord('z') - ord('A') + 1)

    # Function to calculate frequency of characters
    def calculate_frequency(string, offset):
        for char in string:
            index = ord(char) - offset
            if 0 <= index < len(frequency_differences):
                frequency_differences[index] += 1

    # Calculate Frequency Differences
    calculate_frequency(processed_first_string, ord('A'))
    calculate_frequency(processed_second_string, ord('A'))

    # Determine Result
    for char in range(len(frequency_differences)):
        if frequency_differences[char] < 0:
            print("NO")
            return
    
    print("YES")

if __name__ == "__main__":
    main()
