def main():
    # Receive Input
    first_string = input()
    second_string = input()
    
    # Process Strings by removing spaces
    processed_first = first_string.replace(" ", "")
    processed_second = second_string.replace(" ", "")
    
    # Initialize Frequency Count
    frequency_differences = []
    
    # Character Frequency Calculation
    for char in range(ord('A'), ord('z') + 1):  # ASCII values from 'A' to 'z'
        character = chr(char)
        first_count = processed_first.count(character)
        second_count = processed_second.count(character)
        difference = first_count - second_count
        frequency_differences.append(difference)
    
    # Evaluate Results
    negative_count = sum(1 for diff in frequency_differences if diff < 0)
    
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Example of how to call the main function if needed
# main()
