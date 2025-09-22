def main():
    # Get two input strings containing numbers from the user
    input1 = get_user_input()
    input2 = get_user_input()
    
    # Split the input strings into lists of substrings
    numbers1 = split_string(input1)
    numbers2 = split_string(input2)
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the substrings to integers
        value1 = convert_to_integer(numbers1[index])
        value2 = convert_to_integer(numbers2[index])
        
        # If the two values are not equal, increment the difference counter
        if value1 != value2:
            difference_count += 1 
    
    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

def get_user_input():
    # Return user input as a string
    return input()

def split_string(input):
    # Return a list of substrings split by white space
    return input.split()

def convert_to_integer(string_value):
    # Return the integer representation of the string
    return int(string_value)

# Entry point of the program
if __name__ == "__main__":
    main()
