with open("books/frankenstein.txt") as f:
    file_content = f.read()

def count(file_words):
    words = file_words.split()
    return len(words)

def count_char(file_words):
    lowered_chars = file_words.lower()
    char_count ={}
    for char in lowered_chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] =1
    
    return char_count

def report(file_words):
    
    print("-- Report of books/frankenstein.txt --")
    print(f"Number of words in the document: {count(file_content)}") 
    char_count = count_char(file_words)
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times.")
    
    print("-- End report --")

report(file_content)    


