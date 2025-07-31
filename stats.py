def sort_char_counts(char_counts):
    """Return a list of dicts sorted by count descending, each with 'char' and 'num' keys."""
    sorted_list = [
        {"char": char, "num": count} for char, count in char_counts.items()
    ]
    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list
def count_characters(text):
    """Return a dictionary with the count of each character (case-insensitive) in the text."""
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def count_words(text):
    """Return the number of words in the given text string."""
    return len(text.split())
