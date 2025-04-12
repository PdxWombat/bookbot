def get_book_text(path_to_file):
    try:
        print(f"Attempting to open: {path_to_file}")
        with open(path_to_file) as f:
            file_contents = f.read()
        print(f"Successfully read {len(file_contents)} characters from file")
        return file_contents
    except Exception as e:
        print(f"Error reading {path_to_file}: {e}")
        raise

import sys
from stats import word_count, count_characters, sort_character_counts

def main(script_name, path):
    book = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    # Count words
    word_count_result = word_count(book)
    print(f"The book has {word_count_result} words.")
    
    # Count characters
    char_counts = count_characters(book)
    
    # Sort the character counts
    sorted_chars = sort_character_counts(char_counts)
    
    # Print the character counts
    print("\nHere is a report of the letters from most common to least common:")
    for char in sorted_chars:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['count']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # sys.argv[0] is the script name, sys.argv[1] is the book path
    main(sys.argv[0], sys.argv[1])
