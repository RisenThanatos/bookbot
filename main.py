def create_report(word_count, char_list, filepath):
    report = f"--- Begin report of {filepath} ---\n"
    report += f"{word_count} words found in the document\n\n"

    for char_dict in char_list:
        report += f"The {char_dict['char']} character was found {char_dict['count']} times\n"

    report += "--- End report ---"
    return report


def convert_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list


def count_characters(text):
    characters = {}
    lowercase = text.lower()
    for char in lowercase:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def count_words(text):
    words = text.strip().split()
    count = 0
    for word in words:
        count += 1
    return count


def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        filepath = f.name

        word_count = count_words(file_contents)

        char_dict = count_characters(file_contents)

        char_list = convert_to_list(char_dict)

        report = create_report(word_count, char_list, filepath)

        print(report)


main()