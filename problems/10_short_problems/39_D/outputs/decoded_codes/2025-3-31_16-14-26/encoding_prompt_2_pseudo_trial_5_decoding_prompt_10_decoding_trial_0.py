def main():
    # Step 1: Read input from the user
    input_string1 = input()
    input_string2 = input()
    
    # Step 2: Split input strings into lists of tokens
    tokens1 = input_string1.split()
    tokens2 = input_string2.split()
    
    # Step 3: Initialize the difference counter
    difference_count = 0
    
    # Step 4: Compare the first three entries of both lists
    for index in range(3):
        value_from_first_input = int(tokens1[index])
        value_from_second_input = int(tokens2[index])
        
        # Count the differences between the two inputs
        if value_from_first_input != value_from_second_input:
            difference_count += 1
    
    # Step 5: Check the number of differences and output result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
