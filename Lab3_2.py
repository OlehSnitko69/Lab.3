word = input("Введіть слово: ")

cleaned_word = ''.join(char for char in word if char.isalpha())

print(f"Слово після видалення небуквених символів: {cleaned_word}")
