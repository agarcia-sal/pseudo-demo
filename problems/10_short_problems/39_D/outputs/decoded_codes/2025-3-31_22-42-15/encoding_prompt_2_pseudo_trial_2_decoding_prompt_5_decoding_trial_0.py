def main():
    # Prompt the user for input
    first_input = input()
    second_input = input()
    
    # Split the input into separate components
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0
    
    # Compare the components from both input lists
    for index in range(3):
        # Convert current items to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check for differences
        if first_value != second_value:
            difference_count += 1
    
    # Determine the output based on differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Note: It's recommended to test the code with different input cases to ensure its correctness.
# Test cases:
# Input: "1 2 3" "1 2 4" -> Output: "YES"
# Input: "1 2 3" "4 5 6" -> Output: "NO"
