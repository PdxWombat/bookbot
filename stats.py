def word_count(book_text):
    count = len(book_text.split())
    #print(f"{count} words found in the document")
    return count

def count_characters(text):
    """Return a dictionary with the number of times each character appears in the text."""
    text = text.lower()
    character_counts = {}

    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

def sort_character_counts(character_counts):
    """Return a list of dictionaries sorted by character count (descending)."""
    sorted_chars = []

    for char, count in character_counts.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_chars.append({'char': char, 'count': count})

    sorted_chars.sort(key=lambda item: item['count'], reverse=True)
    return sorted_chars

