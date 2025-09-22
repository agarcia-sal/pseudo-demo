def check_character_frequency_difference():
    # Initialize two lists to store the cleaned input strings
    s1 = []
    s2 = []
    
    # Read and clean the first input string
    first_string = input()
    cleaned_first_string = first_string.replace(" ", "")
    s1.append(cleaned_first_string)

    # Read and clean the second input string
    second_string = input()
    cleaned_second_string = second_string.replace(" ", "")
    s2.append(cleaned_second_string)

    # Initialize a frequency difference list
    freqs = []

    # Iterate through the character codes from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        # Calculate the difference in occurrence of the character in s1 and s2
        count_s1 = cleaned_first_string.count(char)
        count_s2 = cleaned_second_string.count(char)
        freqs.append(count_s1 - count_s2)

    # Check if there are no negative values in the freqs list
    if all(freq >= 0 for freq in freqs):
        print("YES")
    else:
        print("NO")

# Call the function to execute the logic
check_character_frequency_difference()
