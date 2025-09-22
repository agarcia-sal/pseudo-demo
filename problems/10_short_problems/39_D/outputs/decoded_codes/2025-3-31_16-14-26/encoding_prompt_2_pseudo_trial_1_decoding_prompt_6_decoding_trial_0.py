def do_main():
    # Prompt for User Input and store it in variables
    input_string_1 = input()
    input_string_2 = input()
    
    # Process the Input: Split the input strings into lists of values
    list_of_values_1 = input_string_1.split()
    list_of_values_2 = input_string_2.split()
    
    # Initialize a Counter for differences
    difference_count = 0
    
    # Compare Values for the first three indices
    for index in range(3):
        value_a = int(list_of_values_1[index])  # Convert to integer
        value_b = int(list_of_values_2[index])  # Convert to integer
        
        # Increment the difference count if values are different
        if value_a != value_b:
            difference_count += 1
    
    # Output the Result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the Program when script is run as standalone
if __name__ == "__main__":
    do_main()
