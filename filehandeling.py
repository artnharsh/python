
def count_words_characters_lines_frequency(file_name, words_list):
    total_characters, total_words, total_lines = 0, 0, 0
    word_frequency = {word.lower(): 0 for word in words_list}
    with open(file_name, 'r') as file:
        for line in file:
            total_characters += len(line)
            total_words += len(line.split())
            total_lines += 1
            line_words = line.lower().split()
            for word in line_words:
                if word in word_frequency:
                    word_frequency[word] += 1

    print("Total Characters:", total_characters)
    print("Total Words:", total_words)
    print("Total Lines:", total_lines)
    print("Word Frequencies:")
    for word, freq in word_frequency.items():
        print(f"{word}: {freq}")

file_name = "HarshFileHandling.txt"
words_list = ['python', 'program']

count_words_characters_lines_frequency(file_name, words_list)
