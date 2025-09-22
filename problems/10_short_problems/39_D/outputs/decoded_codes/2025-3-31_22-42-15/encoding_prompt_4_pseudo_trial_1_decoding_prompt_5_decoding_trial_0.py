def do_main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize the result counter for mismatches
    mismatch_count = 0
    
    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check for mismatches
        if first_value != second_value:
            mismatch_count += 1
            
    # Determine the output based on mismatch count
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()
