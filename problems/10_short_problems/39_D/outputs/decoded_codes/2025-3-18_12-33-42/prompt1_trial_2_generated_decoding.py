def main():
    # Read two lines of input representing two sequences of numbers
    first_sequence = input()
    second_sequence = input()
    
    # Split the input into individual components
    first_list = first_sequence.split()  # Converts the string into a list of strings
    second_list = second_sequence.split()  # Converts the string into a list of strings
    
    mismatch_count = 0  # Initialize a counter for mismatches
    
    # Iterate over the first three elements of both lists
    for index in range(3):  
        number_from_first = int(first_list[index])  # Convert to integer
        number_from_second = int(second_list[index])  # Convert to integer
        
        # Check if the corresponding numbers are different
        if number_from_first != number_from_second:  
            mismatch_count += 1  # Increase the mismatch counter
            
    # Decide the result based on the number of mismatches
    if mismatch_count < 3:  
        print("YES")  # Less than three mismatches means a certain condition is met
    else:
        print("NO")  # Three or more mismatches means the condition is not met
        
# Start the program execution
main()
