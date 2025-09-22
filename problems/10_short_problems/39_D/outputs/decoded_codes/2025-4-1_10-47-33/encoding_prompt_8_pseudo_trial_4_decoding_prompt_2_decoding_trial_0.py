def main():
    # Read two lines of input from the user, representing two sets of numbers
    first_input = user_input()
    second_input = user_input()
    
    # Split the input strings into lists of numbers
    numbers_from_first_input = split(first_input)
    numbers_from_second_input = split(second_input)
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three numbers from both inputs
    for index in range(3):  # Using range(3) to iterate through indices 0 to 2
        # Convert the current number from the first input to an integer
        number_from_first_input = convert(numbers_from_first_input[index])
        
        # Convert the current number from the second input to an integer
        number_from_second_input = convert(numbers_from_second_input[index])
        
        # Check if the numbers from both inputs are different
        if number_from_first_input != number_from_second_input:
            # Increment the difference counter
            difference_count += 1
            
    # Evaluate the total number of differences
    if difference_count < 3:
        # Output "YES" if there are fewer than three differences
        print("YES")
    else:
        # Output "NO" if there are three or more differences
        print("NO")

def user_input():
    # return input from the user
    return input()

def split(input_string):
    # return a list of words from the input_string
    return input_string.split()

def convert(string_value):
    # return the integer value of string_value
    return int(string_value)

# Call the main function to execute
if __name__ == "__main__":
    main()
