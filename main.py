import sys

from stats import word_count, letter_count, sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit

bookpath = sys.argv[1]

#bookpath = input("Enter the path to the book file (or press Enter to use books/frankenstein.txt):")
#if not bookpath:    
    #bookpath = "books/frankenstein.txt"

def get_book_text(bookpath):
    try:
        with open(bookpath) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {bookpath} was not found.")
        return ""
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return ""

def main():
    book = get_book_text(bookpath)
    if not book:
        print("No content to analyse. Exiting")
        return
    words = word_count(book)
    letters = letter_count(book)
    sorted = sort_dict(letters)

    print("============ BOOKBOT ============")
    print(f"Analysing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in sorted:
        line = f"{dict["char"]}" + ": " + f"{dict["num"]}"
        print(line)
    print("============= END ===============")

main()