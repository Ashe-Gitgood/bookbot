# bookboi

import sys
from stats import get_num_words, get_num_chars, sorted_char_count, print_report, print_counts

print(sys.argv)

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    book_text = ""
    
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():
    filepath = sys.argv[1]
    
    book_text = get_book_text(sys.argv[1])

    num_words = get_num_words(book_text)
    
    num_chars = get_num_chars(book_text)

    sorted_chars = sorted_char_count(num_chars)

    report = print_report(filepath, num_words, sorted_chars)

    print(report)

    

main()

