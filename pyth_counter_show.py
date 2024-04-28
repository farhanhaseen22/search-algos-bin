from collections import Counter

letters = Counter("mississippi")
letters["p"]

letters["s"]


for letter in letters:
    print(letter, letters[letter])

for letter in letters.keys():
    print(letter, letters[letter])

for count in letters.values():
    print(count)

for letter, count in letters.items():
    print(letter, count)


def print_ascii_bar_chart(data, symbol="#"):
    counter = Counter(data).most_common()
    chart = {category: symbol * frequency for category, frequency in counter}
    max_len = max(len(category) for category in chart)
    for category, frequency in chart.items():
        padding = (max_len - len(category)) * " "
        print(f"{category}{padding} |{frequency}")

