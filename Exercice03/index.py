words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowel_counts = []

def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

for word in words:
    num_vowels = count_vowels(word)
    vowel_counts.append((word, num_vowels))

print(vowel_counts)