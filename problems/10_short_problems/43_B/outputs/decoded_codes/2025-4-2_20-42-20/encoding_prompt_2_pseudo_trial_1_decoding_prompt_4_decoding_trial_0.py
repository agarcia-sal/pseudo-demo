def main():
    # Step 1: Input Reading
    first_string = input()
    second_string = input()

    # Step 2: String Preprocessing
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")

    # Step 3: Frequency Calculation
    character_frequencies = []
    for char in range(ord('A'), ord('z') + 1):
        count_first = cleaned_first_string.count(chr(char))
        count_second = cleaned_second_string.count(chr(char))
        difference = count_first - count_second
        character_frequencies.append(difference)

    # Step 4: Result Evaluation
    negative_count = sum(1 for freq in character_frequencies if freq < 0)
    
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Run the main function to execute the program
main()
