def mc(number_of_items, bucket_size):
    # Calculate how many full buckets there are and any leftover items
    full_buckets = number_of_items // bucket_size
    leftover_items = number_of_items % bucket_size
    
    # If there are leftover items, calculate adjusted total to account for them
    if leftover_items > 0:
        return leftover_items * (full_buckets + 1)
    else:
        return number_of_items

def main():
    # Read input integers for total items and bucket size
    total_items = int(input())        # Total number of items
    bucket_capacity = int(input())    # Capacity of each bucket
    divisor = int(input())             # Divisor for the mc calculation
    
    # Calculate the product of the results from two calls to the mc function
    result = mc(total_items, divisor) * mc(bucket_capacity, divisor)
    
    # Output the result
    print(result)

# Call the main function to execute the program
main()
