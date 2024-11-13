def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words_in_text(book_text)
    char_count = count_characters_in_text(book_text)
    sorted_list = sort_list(char_count)
    print_report(word_count, sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_text(text):
    list_of_words = text.split()
    return len(list_of_words)
    
def count_characters_in_text(text):
    char_count = {}
    lowercase_text = text.lower()
    
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_nums(alpha_list):
    return alpha_list["num"]

def sort_list(char_count):
    alpha_list = []
    char_dict = {}

    for char in char_count:
        if char.isalpha():
            char_dict["name"] = char
            char_dict["num"] = char_count[char]
            alpha_list.append(char_dict.copy())
    
    alpha_list.sort(reverse=True, key=sort_nums)
    return alpha_list

def print_report(word_count, sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"{word_count} words found in the document")
    print()

    for char in sorted_list:
        print(f"The '{char["name"]}' character was found {char["num"]} times.")

    print()
    print("--- End report ---")


main()

