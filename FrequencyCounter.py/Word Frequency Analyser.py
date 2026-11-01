import string

stop_words = {
    "the", "is", "a", "an", "and",
    "of", "to", "in", "it", "for",
    "on", "are", "was", "were", "be",
    "this", "that", ".", "as", "at"
}

name = input("Hello, please enter your name: ")
print("Hello, " + name.title() + "!" +
      " You're welcome to Word Frequency Analyser! Please enter your text below and I will analyse it for you."
      " Press Enter to continue.")

text = input("Type or paste your text here: ")


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return words


words = text.split()
words = [word for word in words if word not in stop_words]


total_words = len(words)
print("Here are the words in your text:", words)
print(f"\nTotal number of words: {total_words}")


word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

if word_counts:
    highest_frequency = max(word_counts.values())

    most_frequent_words = [
        word for word, count in word_counts.items()
        if count == highest_frequency
    ]

    print(f"Highest frequency: {highest_frequency}")
    print("Most frequent word(s):", ", ".join(most_frequent_words))
else:
    print("\nNo words found in the text to analyse.")


unique_words = len(word_counts)
print(f"\nTotal number of unique words: {unique_words}")

sorted_words = sorted(
    word_counts.items(),
    key=lambda item: item[1],
    reverse=True)

print("\nWord frequencies:")
if total_words == 0:
    print("No words to analyse.")
else:
    for word, count in sorted_words:
        percentage = (count / total_words) * 100
        print(f"{word}: {count} ({percentage:.2f}%)")
