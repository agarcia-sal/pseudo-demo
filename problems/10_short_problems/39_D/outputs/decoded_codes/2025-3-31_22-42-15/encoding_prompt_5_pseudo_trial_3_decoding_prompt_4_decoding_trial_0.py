def compare_inputs_and_determine_result():
    # Prompt the user for two strings of input
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of numbers
    first_list = list(map(int, first_input.split()))
    second_list = list(map(int, second_input.split()))
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding positions in the two lists
    for i in range(3):  # Since we expect three integers in each input
        if first_list[i] != second_list[i]:
            difference_count += 1
            
    # Check the total number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences means the sequences are similar enough
    else:
        print("NO")   # 3 or more differences indicate significant divergence

# Main execution starts here
if __name__ == "__main__":
    compare_inputs_and_determine_result()
