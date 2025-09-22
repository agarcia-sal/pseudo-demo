def main():
    # Step 1: Get input from the user
    input_string1 = input()  # User inputs the first line of text
    input_string2 = input()  # User inputs the second line of text

    # Step 2: Prepare lists of characters by removing spaces
    s1 = [char for char in input_string1 if char != ' ']
    s2 = [char for char in input_string2 if char != ' ']

    # Step 3: Calculate frequency differences for characters 'A' to 'z'
    freqs = []
    for ascii_value in range(ord('A'), ord('z') + 1):  # Include 'z'
        count_in_s1 = s1.count(chr(ascii_value))
        count_in_s2 = s2.count(chr(ascii_value))
        
        # Calculate the difference in counts
        difference = count_in_s1 - count_in_s2
        freqs.append(difference)

    # Step 4: Check for any negative frequencies
    has_negative_frequency = any(frequency < 0 for frequency in freqs)

    # Step 5: Print result based on frequencies
    if not has_negative_frequency:
        print("YES")  # All characters in input_string1 are balanced against input_string2
    else:
        print("NO")   # Some characters in input_string1 exceed those in input_string2

# Run the main function
if __name__ == "__main__":
    main()
