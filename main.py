###Создайте программу, которая считает,
#сколько раз в строке введенного текста встречается слово 'Python'. Используйте цикл.
text=str(input(r"Введите текст (несколько строк, разделённых \n): "))
lines = text.split("\\n")
print(lines)
py="Python"
# Подсчёт количества вхождений слова "Python" в каждой строке
for i, line in enumerate(lines):
    count = line.count(py)
    print(f"Количество слов 'Python' в строке {i + 1}: {count}")
