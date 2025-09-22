def main_procedure():
    # Get input from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize counter for differences
    difference_count = 0 
    
    # Compare the numbers in both lists
    for index in range(3):
        # Convert the current element from both lists to integers
        number_from_first_list = int(first_list[index])
        number_from_second_list = int(second_list[index])
        
        # Check if the numbers are different
        if number_from_first_list != number_from_second_list:
            # Increase the difference count if they are not equal
            difference_count += 1
            
    # Determine the final output based on the count of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences means they are considered similar
    else:
        print("NO")   # 3 or more differences means they are considered different

# Start executing the main procedure when the program runs
main_procedure()
