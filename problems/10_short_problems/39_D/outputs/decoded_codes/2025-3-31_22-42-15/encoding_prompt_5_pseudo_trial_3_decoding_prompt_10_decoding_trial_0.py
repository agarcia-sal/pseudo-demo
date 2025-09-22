def compare_inputs_and_determine_result():
    # Prompt the user for the first input string and store it
    first_input = input()
    # Prompt the user for the second input string and store it
    second_input = input()
    
    # Split the input strings into lists of integers
    first_list = list(map(int, first_input.split()))
    second_list = list(map(int, second_input.split()))
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding positions in the two lists
    for index in range(3):
        first_number = first_list[index]
        second_number = second_list[index]
        
        # If the numbers do not match, increase the difference counter
        if first_number != second_number:
            difference_count += 1
            
    # Check the total number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences means the sequences are similar enough
    else:
        print("NO")   # 3 or more differences indicate significant divergence

# Main execution starts here
if __name__ == "__main__":
    compare_inputs_and_determine_result()
