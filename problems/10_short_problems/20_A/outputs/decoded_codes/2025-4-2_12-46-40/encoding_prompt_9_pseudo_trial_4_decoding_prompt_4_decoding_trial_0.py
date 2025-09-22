def normalize_path(input_path):
    """Normalizes the input file path by removing redundant separators."""
    # Remove any leading and trailing whitespace
    input_path = input_path.strip()
    
    # Split the path into parts using '/' as a separator and filter out empty segments
    parts = [part for part in input_path.split('/') if part]
    
    # Join the parts back together with a single '/'
    normalized_path = '/'.join(parts)
    
    return normalized_path

def main():
    # Step 1: Read entire file path input
    file_path = input()
    
    # Step 2: Normalize the file path
    normalized_path = normalize_path(file_path)
    
    # Step 3: Ensure that the normalized path starts with a single forward slash
    if normalized_path.startswith('//'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Step 4: Output the final normalized path
    print(normalized_path)

# Execute the main function
if __name__ == "__main__":
    main()
