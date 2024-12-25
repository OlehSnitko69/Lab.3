sentence = input("Введіть речення: ")

words = sentence.split()

word_count = {}

for word in words:
    cleaned_word = ''.join(char for char in word if char.isalpha()).lower()
    if cleaned_word:
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

unique_words = [word for word, count in word_count.items() if count == 1]

if unique_words:
    print("Слова, які зустрічаються в реченні один раз:")
    print(", ".join(unique_words))
else:
    print("Усі слова повторюються більше одного разу.")
