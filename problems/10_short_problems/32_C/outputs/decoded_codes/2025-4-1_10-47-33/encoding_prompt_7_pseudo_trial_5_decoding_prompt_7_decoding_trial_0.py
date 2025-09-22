def main():
    # Read input integers for total items and bucket capacity
    total_items = int(input())
    bucket_capacity = int(input())
    divisor = int(input())

    # Calculate the product of the results from two calls to the mc function
    result = mc(total_items, divisor) * mc(bucket_capacity, divisor)
    
    # Output the result
    print(result)

def mc(number_of_items, bucket_size):
    # Calculate how many full buckets and leftover items
    full_buckets = number_of_items // bucket_size  # Calculate the number of full buckets
    leftover_items = number_of_items % bucket_size  # Calculate the leftover items

    # If there are any leftover items, calculate the total items to account for them
    if leftover_items > 0:
        # Return the adjusted count for leftover items
        return leftover_items * (full_buckets + 1)
    else:
        return number_of_items  # Return the original count if no leftovers

# Call main function to execute the code
if __name__ == "__main__":
    main()
