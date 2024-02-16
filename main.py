def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words():
    book = get_book_text()
    words = book.split()
    counter = len(words)
    return counter

def letter_count():
    book_dict = {}
    text = get_book_text()
    letters = text.lower()
    for letter in letters:
        if letter not in book_dict:
            book_dict[letter] = 1
        else:
            book_dict[letter] += 1
    letter_list = [{"name": char, "num": count} for char, count in book_dict.items() if char.isalpha()]
    letter_list.sort(key=lambda book_dict: book_dict["name"])
    return letter_list

def main():
    data = {
        'word_count': count_words(),
        'character_count': letter_count()
    }
    print(f'This book has {data["word_count"]} words')

    print("Character counts:")
    for count in data["character_count"]:
        print(f"The '{count['name']}' character was found {count['num']} times")
    
if __name__ == "__main__":
    print(main())

