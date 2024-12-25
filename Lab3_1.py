string = input("Введіть рядок: ")

if len(string) >= 2:
    second_last_char = string[-2]
    print(f"Передостанній символ рядка: {second_last_char}")
else:
    print("Рядок занадто короткий для отримання передостаннього символу.")
