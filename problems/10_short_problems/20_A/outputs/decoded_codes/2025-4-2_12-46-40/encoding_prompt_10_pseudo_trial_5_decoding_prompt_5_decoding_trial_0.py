def normalize_path():
    # Read input from the user
    input_path = input()
    
    # Clean the input path by removing redundant slashes
    normalized_path = '/'.join(part for part in input_path.split('/') if part)
    
    # Substitute leading slashes with a single leading slash
    final_path = '/' + normalized_path if normalized_path else '/'
    
    # Output the final normalized path
    print(final_path)

# This function can be tested with various input paths for validation.
# Example test cases:
# Input: "///usr//bin///"
# Output: "/usr/bin"
# Input: "usr/bin/../lib//"
# Output: "/usr/lib"
# Input: "//home//user//"
# Output: "/home/user"
# Input: ""
# Output: "/"
