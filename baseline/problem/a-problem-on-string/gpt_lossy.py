from collections import Counter

try:
    # Read input values
    sequence_length = int(input("Enter sequence length: "))
    sequence = list(map(int, input("Enter the sequence: ").split()))
    no_of_queries = int(input("Enter number of queries: "))
    
    # Initialize map (using Counter for frequency counting)
    freq_map = Counter(sequence)
    
    # Process each query
    for _ in range(no_of_queries):
        start, end = map(int, input("Enter start and end values: ").split())
        
        # Check if start and end are different
        if start != end:
            print(freq_map[start] * freq_map[end])
        else:
            # If start == end, calculate combination count
            print(freq_map[start] * (freq_map[start] - 1) // 2)

except Exception:
    pass
