def doMain():
    # Read the first input line and store it as firstInput
    first_input = input()
    
    # Read the second input line and store it as secondInput
    second_input = input()
    
    # Split firstInput into a list of strings
    first_list = first_input.split()
    
    # Split secondInput into a list of strings
    second_list = second_input.split()
    
    # Initialize a variable to count mismatches
    mismatch_count = 0
    
    # For each index from 0 to 2 (inclusive)
    for index in range(3):
        # Convert the values to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check for mismatches
        if first_value != second_value:
            mismatch_count += 1
            
    # If fewer than 3 mismatches, output "YES"
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    doMain()
