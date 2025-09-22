def main():
    # Step 1: Input the number of elements
    n = int(input())  # User input for n, assuming it's a non-negative integer
    if n < 0:
        raise ValueError("Number of elements must be a non-negative integer.")

    # Step 2: Create a boolean list initialized to True
    boolean_list = [True] * n
    
    # Step 3: Initialize counter variables
    index = 0
    step = 1

    # Step 4: Process the boolean list
    while step <= 500000:
        if boolean_list[index]:
            boolean_list[index] = False
        
        # Update step and index for the next iteration
        step += 1
        index = (index + step) % n  # Update index, wrap around if needed

    # Step 5: Check for remaining TRUE values in the list
    remaining_true = [value for value in boolean_list if value]

    # Step 6: Output the result based on the length of remainingTrue
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Ensure the main function runs when this script is executed
if __name__ == "__main__":
    main()
