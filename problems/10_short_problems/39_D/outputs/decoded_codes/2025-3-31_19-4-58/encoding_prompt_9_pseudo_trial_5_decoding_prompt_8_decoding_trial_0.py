def main():
    # Get two lines of input representing two sets of numbers
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    first_numbers = first_input.split()
    second_numbers = second_input.split()
    
    difference_count = 0  # Initialize a counter for differences

    # Compare the numbers in the two lists
    for index in range(3):
        # Convert the current strings to integers for comparison
        first_value = int(first_numbers[index])
        second_value = int(second_numbers[index])
        
        # Check if the current numbers are different
        if first_value != second_value:
            # Increment the difference counter if they are not the same
            difference_count += 1
                
    # Determine the similarity based on the count of differences
    if difference_count < 3:
        print("YES")  # They are similar
    else:
        print("NO")  # They are not similar
            
# Start the program execution
main()
