import sys

from stats import count_words, count_characters, sort_char_counts
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_char_counts(char_counts)
    for item in sorted_char_counts:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")


if __name__ == "__main__":
    main()
