def string_character_comparison():
    # Step 1: Input Reading
    first_string = input()
    second_string = input()
    
    # Step 2: String Preprocessing
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")
    
    # Step 3: Frequency Calculation
    character_frequencies = []
    for char in range(ord('A'), ord('z') + 1):
        char = chr(char)
        count_first = cleaned_first_string.count(char)
        count_second = cleaned_second_string.count(char)
        frequency_difference = count_first - count_second
        character_frequencies.append(frequency_difference)
    
    # Step 4: Result Evaluation
    negative_count = sum(1 for freq in character_frequencies if freq < 0)
    
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# This part gives control to the execution context and allows the function to be called.
if __name__ == "__main__":
    string_character_comparison()
