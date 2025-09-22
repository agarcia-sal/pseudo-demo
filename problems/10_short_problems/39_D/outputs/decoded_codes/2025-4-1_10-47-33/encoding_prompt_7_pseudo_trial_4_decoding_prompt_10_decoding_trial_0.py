def main():
    # Read two input strings from the user
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of strings
    first_tokens = first_input.split()
    second_tokens = second_input.split()
    
    # Initialize a difference counter
    difference_counter = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the tokens to integers
        first_value = int(first_tokens[index])
        second_value = int(second_tokens[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_counter += 1

    # If the number of differences is less than 3
    if difference_counter < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
