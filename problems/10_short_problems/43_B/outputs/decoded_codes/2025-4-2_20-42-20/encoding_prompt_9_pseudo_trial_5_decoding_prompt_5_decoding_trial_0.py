# Function to compare the character frequencies of two input strings
def compare_character_frequencies():
    # Step 1: Receive Input
    first_string = input()
    second_string = input()
    
    # Step 2: Process Input Strings
    first_processed = first_string.replace(" ", "")
    second_processed = second_string.replace(" ", "")
    
    # Step 3: Initialize Frequency List
    frequency_difference = [0] * (ord('z') - ord('A') + 1)
    
    # Step 4: Calculate Character Frequencies
    for char in range(ord('A'), ord('z') + 1):
        first_count = first_processed.count(chr(char))
        second_count = second_processed.count(chr(char))
        # Calculate the frequency difference
        frequency_difference[char - ord('A')] = first_count - second_count
    
    # Step 5: Check Conditions
    if all(diff >= 0 for diff in frequency_difference):
        print("YES")  # All characters in firstProcessed meet or exceed those in secondProcessed
    else:
        print("NO")   # Some characters in secondProcessed exceed those in firstProcessed

# Test the function with different inputs
# compare_character_frequencies()  # Uncomment to run the function
