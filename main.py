def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()  

def count_words(text):
    return len(text.split())
    
def main():
    book_path = "./books/Frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words") 

main ()

