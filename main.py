def count_characters(text):
    characters = {}
    lowercase = text.lower()
    for char in lowercase:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    print(characters)

def count_words(text):
    words = text.strip().split()
    count = 0
    for word in words:
        count += 1
    print(count)

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        count_characters(file_contents)

        count_words(file_contents)

    print(file_contents) # replace "file_contents" with "1" here for testing


main()