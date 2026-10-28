import string

text = input("Введіть рядок символів (укр/англ літери, цифри, знаки): ")

unique_text = ""
for char in text:
    if char not in unique_text:
        unique_text += char

letters = set()
digits = set()
punctuations = set()

for char in text:
    if char.isalpha():
        letters.add(char)
    elif char.isdigit():
        digits.add(char)
    elif char in string.punctuation or char in "«»—–…":
        punctuations.add(char)

print("\n" + "-" * 30)
print(f"Ви ввели: {text}")
print(f"Рядок без повторів: {unique_text}")
print(f"Множина літер: {letters}")
print(f"Множина цифр: {digits}")
print(f"Множина знаків:{punctuations}")
print("-" * 30)