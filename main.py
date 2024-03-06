def main():
    
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    total_words = word_count(file_contents)

    print(f"Book has {total_words} words")

    letters = letter_count(file_contents.lower())

    char_report = []

    for i in letters.keys():
        if i.isalpha():
            char_report.append({"char": i, "count": letters[i] })
    
    char_report.sort(reverse=True, key=sort_on)

    for char in char_report:
        print(f"The {char['char']} character was found {char['count']} times")
    

def sort_on(dict):
    return dict["count"]

def letter_count(text):
    letters = {}
    for l in text:
        if l not in letters.keys():
            letters[l] = 1
        else:
            letters[l] += 1
    return letters

def word_count(text):
    words = len(text.split())
    return words

main()