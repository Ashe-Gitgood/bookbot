

def get_num_words(book_text):
    words = []
    num_words = int

    words = book_text.split()    
    num_words = len(words)

    return num_words

def get_num_chars(book_text):
    char_count = {}
    lowercase = ""

    lowercase = book_text.lower()

    for letter in lowercase:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1

    return char_count

def sorted_char_count(char_count):
    sorted = []
    num = int
    def return_year(d): #have to call in num value for the sorted in a separate fn.
        return d["num"]


    for key, value in char_count.items():
        dict = {}
        
        if key.isalpha() == True:   #remove spaces and symbols from entry
            dict["char"] = f"{key}"
            dict["num"] = value
            sorted.append(dict) 
        
    sorted.sort(reverse=True, key=return_year)    
    
    return sorted

def print_counts(sorted_chars):
    def return_char(sorted_chars):
        return sorted_chars["char"]
    def return_num(sorted_chars):
        return sorted_chars["num"]

    for entry in sorted_chars:
        letter = return_char(entry)
        number = return_num(entry)
        print(f"{letter}: {number}")

def print_report(filepath,num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_counts(sorted_chars)
    print("============= END ===============")

