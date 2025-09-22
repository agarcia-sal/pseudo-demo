# Program to determine if there are any True values left in an array after processing

def main():
    # Step 2: Get an integer input from the user
    n = int(input())
    
    # Step 3: Initialize an array b of size n with all values set to True
    b = [True] * n

    # Step 4: Initialize variables
    index_j = 0  # Tracks the current index in the array
    step_i = 1   # Controls the step increments

    # Step 5: While loop to iterate until step_i exceeds 500000
    while step_i <= 500000:
        if b[index_j]:  # Step 5a: Check if the current index is True
            b[index_j] = False  # Mark it as False
        
        step_i += 1  # Step 5b: Increment the step counter
        index_j = (index_j + step_i) % n  # Step 5c: Update the index with wrap-around
    
    # Step 6: Create an array x to store elements from b that are still True
    x = [value for value in b if value]  # Filter True values from b

    # Step 7: Check the size of x and output results
    if len(x) == 0:  # Step 7a: If x is empty
        print("YES")
    else:  # Step 7b: If x is not empty
        print("NO")

# Run the program
main()
